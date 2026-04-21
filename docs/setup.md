# Setup

## Overview

This document describes how to set up and run the Flask applications on a Raspberry Pi environment.

The setup uses a Python virtual environment, SQLite database, and optional deployment via Nginx and systemd.

---

## 1. Install system dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nginx
```

---

## 2. Clone repository

```bash
git clone <your-repo-url>
cd flask-mini-apps-raspberrypi
```

---

## 3. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Python dependencies

Repeat for each app:

```bash
cd apps/book-tracker
pip install -r requirements.txt
```

Same for:

```bash
cd ../food-tracker
pip install -r requirements.txt
```

---

## 5. Run application (development mode)

Example:

```bash
cd apps/book-tracker
python app.py
```

App should be available at:

```text
http://127.0.0.1:5000
```

---

## 6. systemd service (optional)

Copy example service:

```bash
sudo cp systemd/book-tracker.service /etc/systemd/system/
```

Reload and start:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable book-tracker
sudo systemctl start book-tracker
```

Check status:

```bash
sudo systemctl status book-tracker
```

---

## 7. Nginx reverse proxy (optional)

Copy example config:

```bash
sudo cp nginx/example-routes.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/example-routes.conf /etc/nginx/sites-enabled/
```

Test config:

```bash
sudo nginx -t
```

Reload:

```bash
sudo systemctl reload nginx
```

---

## 8. Notes

* make sure Flask apps are running before testing Nginx routes
* verify correct ports in both Flask app and Nginx config
* always test locally before enabling reverse proxy
* use logs (`journalctl`, Nginx logs) for debugging
