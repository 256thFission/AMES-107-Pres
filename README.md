# East Asia Simulation

A small Flask classroom-simulation app: students join with a participant
number, receive a shifting historical identity across 17 stages of East Asian
history (1894-1945), and vote on period decisions. Every group decides at the
same time, each on its own question, and none of them can see the others. Some
groups hold real state power; others may only advise. A projector page reveals
the results one country at a time.

## Run locally

```
python -m venv .venv
.venv/bin/pip install -r requirements.txt
ADMIN_PASSWORD=x .venv/bin/flask --app app run
```

URLs:

- `/login`: students enter their participant number (1-24)
- `/admin`: presenter controls (password from `ADMIN_PASSWORD`)
- `/results`: projector view of the current decision, drawn as sketchy
  bar charts with roughViz.js (vendored in `static/`, no CDN)

## Editing content

All historical content lives in `config.py`:

- `PARTICIPANTS`: participant numbers and their starting groups
- `STAGES` / `STAGE_LABELS`: ordered stages and display titles
- `ROUNDS`: decisions, one per stage, holding a question per faction
  under `questions`. A faction with no entry sits that round out. Whether a
  faction's vote is binding or advisory is not set here: it comes from
  `resolve_identity` in `app.py`, so the Emperor alone speaks for Qing China
  and the Tsar alone for the Russian Empire.
- `TRANSITIONS`: identity-change notices shown to affected students
- `BRIEFINGS`: private per-faction briefings for every stage

Identities are never mutated; they are computed from `(participant, stage)`
in `app.py`'s `resolve_identity`, so advancing the stage automatically
changes roles, icons and voting rights.

## Deploying to EC2 (Ubuntu)

```
sudo apt install nginx python3-venv
git clone <repo> /home/ubuntu/AMES-sino && cd /home/ubuntu/AMES-sino
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp deploy/.env.example .env   # fill in SECRET_KEY and ADMIN_PASSWORD
sudo cp deploy/east-asia-sim.service /etc/systemd/system/
sudo cp deploy/nginx.conf /etc/nginx/sites-available/east-asia-sim
sudo ln -s /etc/nginx/sites-available/east-asia-sim /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl enable --now east-asia-sim
sudo nginx -t && sudo systemctl reload nginx
```

Gunicorn runs with a single worker (`-w 1`) because all game state is held in
memory in one process. Do not raise the worker count.

## Classroom flow

1. Students go to `/login`, enter their number, and read their briefing.
2. The presenter advances stages and presses OPEN VOTING on `/admin`.
3. Every group votes at once, each on its own question. The presenter watches
   the counts, presses CLOSE VOTING, then reveals the countries one at a time
   with the REVEAL button beside each. `/results` on the projector updates as
   each is revealed. REVEAL ALL and HIDE ALL are there too.
4. NEXT moves to the next stage; affected students see a transition notice.

Restarting the server, or pressing RESET PRESENTATION on `/admin`, clears
all votes and progress. There is no persistent storage.
