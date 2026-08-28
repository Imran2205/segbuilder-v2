#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [[ ! -x .venv/bin/python ]]; then
    echo "Creating local Python environment..."
    python3 -m venv .venv
fi

if ! .venv/bin/python -c "import cv2, dash, flask" >/dev/null 2>&1; then
    echo "Installing SegBuilder dependencies..."
    .venv/bin/python -m pip install -r requirements.txt
fi

exec .venv/bin/python run.py
