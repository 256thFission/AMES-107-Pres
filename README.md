# AMES 107

## Run it

```
./start.sh
```

That builds the virtualenv on first run, picks a free port (macOS keeps port
5000 for AirPlay), prints an admin password, and tells you the address students
type into their phones. Everyone needs to be on the same wifi. Pass your own
password as `./start.sh mypassword` if you would rather choose it.

Manually, if you prefer:

```
python -m venv .venv
.venv/bin/pip install -r requirements.txt
ADMIN_PASSWORD=x .venv/bin/flask --app app run
```

URLs:

- `/login`: students enter their participant number, 1 to however
  many rows `PARTICIPANTS` has in `config.py`
- `/admin`: presenter controls (password from `ADMIN_PASSWORD`)
- `/results`: projector view of the current decision, drawn as sketchy
  bar charts with roughViz.js (vendored in `static/`, no CDN)


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

Identities are computed from `(participant, stage)` by `resolve_identity`
in `app.py`, never stored, so advancing the stage automatically changes
roles, icons and voting rights.
