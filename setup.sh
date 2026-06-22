#!/bin/bash
# Creates a venv and installs dependencies
set -e

python3 -m venv venv
venv/bin/pip install --quiet --upgrade pip
venv/bin/pip install --quiet -r requirements.txt
echo "Setup complete. Run with: venv/bin/python3 webhook_listener.py"
