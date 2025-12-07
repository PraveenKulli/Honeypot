🛡️ Honeypot Web Security System

This project is a Django-based honeypot designed to detect and log unauthorized login attempts. It simulates vulnerable pages to attract attackers and records their behavior for security analysis.

🚀 Features

Fake (decoy) login page

Logs IP address, username, timestamp

Admin dashboard to view attacker logs

Isolated honeypot environment

Django-based and easy to deploy

▶️ Run the Project
git clone <repo-url>
cd honeypot-project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Open in browser:
http://127.0.0.1:8000

📄 Documentation

Full report included: Team_08_Honeypot-Report.pdf

✅ 2. Professional, Clean, Minimal README
Honeypot Web Security System

A Django-powered honeypot that simulates vulnerable login pages to detect, monitor, and analyze unauthorized access attempts.

Key Highlights

Deceptive login interface

Centralized dashboard for viewing intrusion logs

Tracks attempted credentials, source IPs, and timestamps

Safe environment for studying attacker behavior

Built using Django, SQLite, and custom views/models

Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Purpose

This project was developed as part of the Information Security Course Project (2023–24).
It demonstrates the use of honeypots as proactive cybersecurity tools.

✅ 3. Developer-Focused README (Technical & Concise)
Honeypot Detection System (Django)

A web honeypot built with Django to analyze malicious login attempts.
It provides a decoy authentication page and logs all attacker interactions for further threat intelligence.

Technical Features

Django-based honeypot module

Custom views simulating authentication logic

SQLite backend storing attacker metadata

Extended Django admin for viewing logs

ASGI-configured for better concurrency

Installation

git clone <repo-url>

cd honeypot

python -m venv env

source env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
