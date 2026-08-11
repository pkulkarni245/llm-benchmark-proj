@echo off
SETLOCAL EnableDelayedExpansion

echo =======================================================
echo 🏛️ SEBI Compliance AI & RAG System - Auto-Launcher
echo =======================================================

:: Check for Python installation
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not in PATH. Please install Python 3.10+ first.
    pause
    exit /b 1
)

:: Create virtual environment if it does not exist
if not exist ".venv" (
    echo [1/3] Creating virtual environment (.venv)...
    python -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
) else (
    echo [1/3] Virtual environment (.venv) detected.
)

:: Activate virtual environment and install requirements
echo [2/3] Checking and installing required packages from requirements.txt...
call .venv\Scripts\activate.bat
pip install -r requirements.txt --quiet --disable-pip-version-check

:: Launch application server
echo [3/3] Launching SEBI Compliance AI web app on http://localhost:7860/ ...
python -m backend.main

pause
