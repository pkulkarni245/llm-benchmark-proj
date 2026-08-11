#!/bin/bash

echo "======================================================="
echo "🏛️ SEBI Compliance AI & RAG System - Auto-Launcher"
echo "======================================================="

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 could not be found. Please install Python 3.10+."
    exit 1
fi

# Create virtual environment if missing
if [ ! -d ".venv" ]; then
    echo "[1/3] Creating virtual environment (.venv)..."
    python3 -m venv .venv
fi

# Activate virtual environment and install requirements
echo "[2/3] Checking and installing requirements..."
source .venv/bin/activate
pip install -r requirements.txt --quiet

# Launch server
echo "[3/3] Launching web app on http://localhost:7860/ ..."
python -m backend.main
