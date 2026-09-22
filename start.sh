#!/usr/bin/env bash
# Start the simulation. Creates the virtualenv on first run.
#
#   ./start.sh              pick a random admin password and print it
#   ./start.sh mypassword   use your own
#   PORT=8080 ./start.sh    force a port instead of finding a free one

set -euo pipefail
cd "$(dirname "$0")"

PY=""
for candidate in python3.12 python3.11 python3 python; do
    if command -v "$candidate" >/dev/null 2>&1; then PY="$candidate"; break; fi
done
if [ -z "$PY" ]; then
    echo "No Python found. Install Python 3.9 or newer and run this again." >&2
    exit 1
fi

if [ ! -x .venv/bin/python ]; then
    echo "Setting up (once, takes about a minute)..."
    "$PY" -m venv .venv
    .venv/bin/pip install --quiet --upgrade pip
    .venv/bin/pip install --quiet -r requirements.txt
fi

# Port 5000 is taken by AirPlay Receiver on most Macs, so find one that is free.
PORT="${PORT:-$(.venv/bin/python - <<'PY'
import socket
for port in range(5000, 5040):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("0.0.0.0", port))
        except OSError:
            continue
        print(port)
        break
else:
    print(5000)
PY
)}"

ADMIN_PASSWORD="${1:-$(.venv/bin/python -c 'import secrets; print(secrets.token_hex(3))')}"
export ADMIN_PASSWORD
export SECRET_KEY="$(.venv/bin/python -c 'import secrets; print(secrets.token_hex(32))')"

# The address students type into their phones. Falls back to localhost.
LAN_IP="$(.venv/bin/python - <<'PY'
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
except OSError:
    print("localhost")
finally:
    s.close()
PY
)"

cat <<EOF

  EAST ASIA SIMULATION

  Students     http://$LAN_IP:$PORT/login        (same wifi, numbers 1-24)
  Projector    http://localhost:$PORT/results
  You          http://localhost:$PORT/admin      password: $ADMIN_PASSWORD

  Ctrl-C to stop. Votes are held in memory, so stopping clears the game.

EOF

exec .venv/bin/flask --app app run --host 0.0.0.0 --port "$PORT"
