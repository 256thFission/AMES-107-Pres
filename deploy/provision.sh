#!/bin/bash
# Provisions a fresh Ubuntu 24.04 box to serve the simulation.
# Pass as EC2 user-data, or run with sudo on a box you already have.
#
#   ADMIN_PASSWORD=yourpassword sudo -E bash provision.sh
#
# Tested on t4g.nano (ARM). A nano is enough: one gunicorn worker serving a
# class of 24.

set -eux
exec > /var/log/ames-setup.log 2>&1

APP_DIR=/home/ubuntu/AMES-107-Pres
ADMIN_PASSWORD="${ADMIN_PASSWORD:-$(python3 -c 'import secrets;print(secrets.token_hex(4))')}"

export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y python3-venv python3-pip nginx git

if [ ! -d "$APP_DIR" ]; then
    git clone https://github.com/256thFission/AMES-107-Pres.git "$APP_DIR"
fi
cd "$APP_DIR"
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

cat > .env <<ENVEOF
SECRET_KEY=$(python3 -c 'import secrets;print(secrets.token_hex(32))')
ADMIN_PASSWORD=$ADMIN_PASSWORD
ENVEOF
chmod 600 .env
chown -R ubuntu:ubuntu "$APP_DIR"

# nginx runs as www-data and serves /static/ straight off disk. Ubuntu 24.04
# ships /home/ubuntu as drwxr-x---, so without this every asset 404s at the
# proxy and 403s at the file, and the page renders with no CSS and no charts.
# o+x grants traversal only: the home directory still cannot be listed.
chmod o+x /home/ubuntu

cp deploy/east-asia-sim.service /etc/systemd/system/
cp deploy/nginx.conf /etc/nginx/sites-available/east-asia-sim
ln -sf /etc/nginx/sites-available/east-asia-sim /etc/nginx/sites-enabled/east-asia-sim
rm -f /etc/nginx/sites-enabled/default

systemctl daemon-reload
systemctl enable --now east-asia-sim
nginx -t
systemctl restart nginx

echo "AMES SETUP COMPLETE. Admin password: $ADMIN_PASSWORD"
