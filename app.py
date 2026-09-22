import os
import secrets
import threading
from copy import deepcopy
from functools import wraps

from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, session, url_for)

from config import (BRIEFINGS, FACTION_COLORS, FACTION_ORDER, PARTICIPANTS,
                    ROUNDS, STAGE_INDEX, STAGE_LABELS, STAGES, TRANSITIONS)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme")

INITIAL_STATE = {"stage": 0, "round": None, "voting_open": False,
                 "revealed": [], "votes": {},
                 "acknowledged_transitions": set()}
STATE = deepcopy(INITIAL_STATE)
LOCK = threading.Lock()

@app.context_processor
def inject_revealed():
    return {"revealed_key": ",".join(STATE["revealed"])}


FACTION_NAMES = {"china": "China", "taiwan": "Taiwan", "japan": "Japan",
                 "korea": "Korea", "russia": "Russia", "west": "The West"}


def resolve_identity(p, s):
    stage = STAGES[s]
    group = p.get("group")
    out = {"identity": "", "role": "", "icon": "", "voting_mode": "none",
           "faction": "", "briefing": []}
    if group == "china" and p.get("region") == "mainland":
        if s < STAGE_INDEX["qing_collapse"]:
            out.update(identity="Qing China", icon="🐉", faction="china",
                       role="Emperor" if p.get("special") == "emperor" else "Peasant",
                       voting_mode="binding" if p.get("special") == "emperor" else "none")
        else:
            out.update(identity="Republic of China", role="Nationalist",
                       icon="🇨🇳", voting_mode="binding", faction="china")
    elif group == "china" and p.get("region") == "taiwan":
        if s < STAGE_INDEX["shimonoseki"]:
            out.update(identity="Qing China", role="Peasant", icon="🐉",
                       voting_mode="none", faction="china")
        else:
            out.update(identity="Taiwan under Japanese rule",
                       role="Taiwanese subject", icon="🏝️",
                       voting_mode="advisory", faction="taiwan")
    elif group == "japan":
        out.update(identity="Empire of Japan", role="Government", icon="🇯🇵",
                   voting_mode="binding", faction="japan")
    elif group == "korea":
        if s < STAGE_INDEX["shimonoseki"]:
            out.update(identity="Joseon Korea (Qing tributary)",
                       role="Court official", icon="🏯", voting_mode="none",
                       faction="korea")
        elif s < STAGE_INDEX["korea_japanese_rule"]:
            out.update(identity="Independent Korea", role="Government",
                       icon="🇰🇷", voting_mode="binding", faction="korea")
        else:
            out.update(identity="Korea under Japanese rule",
                       role="Colonial subject", icon="🇰🇷",
                       voting_mode="advisory", faction="korea")
    elif group == "russia":
        if s < STAGE_INDEX["russian_collapse"]:
            out.update(identity="Russian Empire", icon="🇷🇺", faction="russia",
                       role="Tsar" if p.get("special") == "tsar" else "Peasant",
                       voting_mode="binding" if p.get("special") == "tsar" else "none")
        else:
            out.update(identity="Soviet Russia", role="Revolutionary", icon="☭",
                       voting_mode="binding", faction="russia")
    elif group == "west":
        out.update(identity="Western Powers", role="Diplomat", icon="🌐",
                   voting_mode="binding", faction="west")
    out["briefing"] = BRIEFINGS.get(stage, {}).get(out["faction"], [])
    return out


def faction_display(faction, stage_idx):
    if faction == "russia" and stage_idx >= STAGE_INDEX["russian_collapse"]:
        return "USSR"
    return FACTION_NAMES.get(faction, faction.title())


def question_for(rnd, faction):
    return rnd["questions"].get(faction) if rnd else None


def round_factions(rnd):
    """Factions that have a question this round, in display order."""
    return [f for f in FACTION_ORDER if f in rnd["questions"]]


def voters_by_faction(round_id):
    """faction -> {"binding": [pid], "advisory": [pid]} for factions that vote."""
    r = ROUNDS[round_id]
    s = STAGE_INDEX[r["stage"]]
    out = {f: {"binding": [], "advisory": []} for f in round_factions(r)}
    for pid, p in PARTICIPANTS.items():
        ident = resolve_identity(p, s)
        bucket = out.get(ident["faction"])
        if bucket is not None and ident["voting_mode"] in bucket:
            bucket[ident["voting_mode"]].append(pid)
    return out


def faction_is_binding(round_id, faction):
    return bool(voters_by_faction(round_id).get(faction, {}).get("binding"))


def round_for_stage(idx):
    stage = STAGES[idx]
    for rid, r in ROUNDS.items():
        if r["stage"] == stage:
            return rid
    return None


def results_visible():
    return bool(STATE["revealed"])


def set_stage(idx):
    idx = max(0, min(len(STAGES) - 1, idx))
    STATE["stage"] = idx
    STATE["round"] = round_for_stage(idx)
    STATE["voting_open"] = False
    STATE["revealed"] = []


set_stage(0)


def pending_transition(pid):
    p = PARTICIPANTS[pid]
    for t in TRANSITIONS:
        if (STAGE_INDEX[t["stage"]] <= STATE["stage"] and t["applies"](p)
                and (pid, t["id"]) not in STATE["acknowledged_transitions"]):
            return t
    return None


def current_participant():
    pid = session.get("participant_id")
    return pid if pid in PARTICIPANTS else None


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return wrapper


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_participant() is not None:
        return redirect(url_for("index"))
    error = None
    if request.method == "POST":
        try:
            pid = int(request.form.get("participant_id", ""))
        except ValueError:
            pid = None
        if pid in PARTICIPANTS:
            session["participant_id"] = pid
            return redirect(url_for("index"))
        error = "That number is not on the class list."
    return render_template("login.html", error=error)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
def index():
    pid = current_participant()
    if pid is None:
        return redirect(url_for("login"))
    p = PARTICIPANTS[pid]
    s = STATE["stage"]
    t = pending_transition(pid)
    if t:
        ts = STAGE_INDEX[t["stage"]]
        prev_ident = resolve_identity(p, ts - 1) if ts > 0 else None
        new_ident = resolve_identity(p, ts)
        return render_template("transition.html", pid=pid, transition=t,
                               prev=prev_ident, new=new_ident,
                               stage=s, voting_open=STATE["voting_open"],
                               results_visible=results_visible())
    ident = resolve_identity(p, s)
    year, title = STAGE_LABELS[STAGES[s]]
    rid = STATE["round"]
    rnd = ROUNDS[rid] if rid else None
    votes = STATE["votes"].get(rid, {}) if rid else {}
    timeline = [{"year": STAGE_LABELS[name][0], "title": STAGE_LABELS[name][1],
                 "state": "past" if i < s else ("current" if i == s else "future")}
                for i, name in enumerate(STAGES)]
    ctx = {
        "pid": pid, "ident": ident, "year": year, "stage_title": title,
        "timeline": timeline,
        "stage": s, "voting_open": STATE["voting_open"],
        "results_visible": results_visible(),
        "round": rnd, "round_id": rid,
        "eligible": False, "advisory": False, "binding": False,
        "my_vote": votes.get(pid),
        "faction_label": faction_display(ident["faction"], s),
        "decider": None,
        "my_question": "", "my_options": {},
    }
    qa = question_for(rnd, ident["faction"])
    if qa:
        ctx["my_question"] = qa["question"]
        ctx["my_options"] = qa["options"]
        if ident["voting_mode"] != "none":
            ctx["eligible"] = True
            ctx["advisory"] = ident["voting_mode"] == "advisory"
            ctx["binding"] = ident["voting_mode"] == "binding"
        elif ident["faction"] == "china" and s < STAGE_INDEX["qing_collapse"]:
            ctx["decider"] = "THE EMPEROR"
        elif ident["faction"] == "russia" and s < STAGE_INDEX["russian_collapse"]:
            ctx["decider"] = "THE TSAR"
    return render_template("student.html", **ctx)


@app.route("/vote", methods=["POST"])
def vote():
    pid = current_participant()
    if pid is None:
        return redirect(url_for("login"))
    rid = STATE["round"]
    option = request.form.get("option")
    if not rid or not STATE["voting_open"]:
        flash("Voting is not open.")
        return redirect(url_for("index"))
    rnd = ROUNDS[rid]
    ident = resolve_identity(PARTICIPANTS[pid], STAGE_INDEX[rnd["stage"]])
    qa = question_for(rnd, ident["faction"])
    if qa is None or ident["voting_mode"] == "none":
        flash("You do not have a vote in this decision.")
        return redirect(url_for("index"))
    if option not in qa["options"]:
        flash("Invalid option.")
        return redirect(url_for("index"))
    with LOCK:
        STATE["votes"].setdefault(rid, {})
        if pid in STATE["votes"][rid]:
            flash("You have already voted.")
            return redirect(url_for("index"))
        STATE["votes"][rid][pid] = option
    return redirect(url_for("index"))


@app.route("/acknowledge", methods=["POST"])
def acknowledge():
    pid = current_participant()
    if pid is None:
        return redirect(url_for("login"))
    tid = request.form.get("transition_id")
    if tid not in {t["id"] for t in TRANSITIONS}:
        return redirect(url_for("index"))
    with LOCK:
        STATE["acknowledged_transitions"].add((pid, tid))
    return redirect(url_for("index"))


@app.route("/api/status")
def api_status():
    return jsonify({"stage": STATE["stage"],
                    "voting_open": STATE["voting_open"],
                    "results_visible": results_visible(),
                    "revealed": ",".join(STATE["revealed"])})


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            session["is_admin"] = True
            return redirect(url_for("admin"))
        error = "Wrong password."
    return render_template("admin_login.html", error=error)


def submission_counts(rid):
    rnd = ROUNDS[rid]
    s = STAGE_INDEX[rnd["stage"]]
    votes = STATE["votes"].get(rid, {})
    rows = []
    for f, buckets in voters_by_faction(rid).items():
        pids = buckets["binding"] + buckets["advisory"]
        if not pids:
            continue
        rows.append({"faction": faction_display(f, s), "key": f,
                     "advisory": not buckets["binding"],
                     "revealed": f in STATE["revealed"],
                     "submitted": sum(1 for pid in pids if pid in votes),
                     "eligible": len(pids)})
    return rows


@app.route("/admin")
@admin_required
def admin():
    s = STATE["stage"]
    rid = STATE["round"]
    rnd = ROUNDS[rid] if rid else None
    rows = submission_counts(rid) if rid else []
    archive = []
    for arid, r in ROUNDS.items():
        if STATE["votes"].get(arid) or STAGE_INDEX[r["stage"]] <= s:
            archive.append({"id": arid, "title": r["title"]})
    return render_template("admin.html", stage=s, total=len(STAGES),
                           year=STAGE_LABELS[STAGES[s]][0],
                           stage_title=STAGE_LABELS[STAGES[s]][1],
                           round=rnd, rows=rows, archive=archive,
                           voting_open=STATE["voting_open"],
                           results_visible=results_visible())


@app.route("/admin/counts")
@admin_required
def admin_counts():
    rid = STATE["round"]
    return jsonify({"round": rid,
                    "rows": submission_counts(rid) if rid else [],
                    "voting_open": STATE["voting_open"],
                    "results_visible": results_visible()})


def _admin_post(action, faction=None):
    with LOCK:
        rid = STATE["round"]
        if action == "open":
            if rid:
                STATE["voting_open"] = True
        elif action == "close":
            STATE["voting_open"] = False
        elif action == "reveal" and rid:
            STATE["voting_open"] = False
            if faction in ROUNDS[rid]["questions"] and faction not in STATE["revealed"]:
                STATE["revealed"].append(faction)
        elif action == "reveal_all" and rid:
            STATE["voting_open"] = False
            for f in round_factions(ROUNDS[rid]):
                if f not in STATE["revealed"]:
                    STATE["revealed"].append(f)
        elif action == "hide":
            STATE["revealed"] = []
        elif action == "next":
            set_stage(STATE["stage"] + 1)
        elif action == "previous":
            set_stage(STATE["stage"] - 1)
        elif action == "reset":
            STATE.clear()
            STATE.update(deepcopy(INITIAL_STATE))
            set_stage(0)
    return redirect(url_for("admin"))


@app.route("/admin/open", methods=["POST"])
@admin_required
def admin_open():
    return _admin_post("open")


@app.route("/admin/close", methods=["POST"])
@admin_required
def admin_close():
    return _admin_post("close")


@app.route("/admin/reveal", methods=["POST"])
@admin_required
def admin_reveal():
    return _admin_post("reveal", request.form.get("faction"))


@app.route("/admin/reveal-all", methods=["POST"])
@admin_required
def admin_reveal_all():
    return _admin_post("reveal_all")


@app.route("/admin/hide", methods=["POST"])
@admin_required
def admin_hide():
    return _admin_post("hide")


@app.route("/admin/next", methods=["POST"])
@admin_required
def admin_next():
    return _admin_post("next")


@app.route("/admin/previous", methods=["POST"])
@admin_required
def admin_previous():
    return _admin_post("previous")


@app.route("/admin/reset", methods=["POST"])
@admin_required
def admin_reset():
    return _admin_post("reset")


def results_context(rid, show=None):
    """show: ordered factions to display, or None for every faction."""
    rnd = ROUNDS[rid]
    s = STAGE_INDEX[rnd["stage"]]
    buckets = voters_by_faction(rid)
    votes = STATE["votes"].get(rid, {})
    order = show if show is not None else round_factions(rnd)

    def verdict(c, options):
        if not any(c.values()):
            return {"kind": "none", "text": ""}
        top = max(c.values())
        winners = [k for k, v in c.items() if v == top]
        if len(winners) > 1:
            return {"kind": "tie", "text": " / ".join(winners)}
        k = winners[0]
        return {"kind": "win", "text": f"{k}: {options[k]}"}

    sections, charts = [], []
    for f in order:
        qa = question_for(rnd, f)
        pids = buckets[f]["binding"] + buckets[f]["advisory"]
        if not qa or not pids:
            continue
        options = qa["options"]
        counts = {k: 0 for k in options}
        for pid in pids:
            if votes.get(pid) in counts:
                counts[votes[pid]] += 1
        pal = FACTION_COLORS.get(f, ["#333"])
        element = f"#chart-{f}"
        sections.append({
            "key": f, "name": faction_display(f, s),
            "binding": bool(buckets[f]["binding"]),
            "question": qa["question"],
            "rows": [{"letter": k, "text": options[k], "count": counts[k]}
                     for k in options],
            "verdict": verdict(counts, options),
            "element": element,
        })
        charts.append({"element": element, "labels": list(options),
                       "values": [counts[k] for k in options],
                       "color": pal[0], "colors": pal})
    return {"round": rnd, "sections": sections, "charts": charts}


@app.route("/results")
def results():
    rid = STATE["round"]
    common = {"stage": STATE["stage"], "voting_open": STATE["voting_open"],
              "results_visible": results_visible()}
    if not rid:
        return render_template("results.html", none=True, **common)
    if not STATE["revealed"]:
        return render_template("results.html", awaiting=True, **common)
    ctx = results_context(rid, show=list(STATE["revealed"]))
    ctx.update(common)
    return render_template("results.html", **ctx)


@app.route("/results/<round_id>")
def results_archive(round_id):
    if round_id not in ROUNDS:
        abort(404)
    ctx = results_context(round_id)
    ctx.update(stage=STATE["stage"], voting_open=STATE["voting_open"],
               results_visible=results_visible())
    return render_template("results.html", **ctx)


if __name__ == "__main__":
    app.run()
