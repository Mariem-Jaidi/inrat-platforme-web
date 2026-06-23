@echo off
cd /d "%~dp0"
if not exist venv\Scripts\activate.bat (
    echo Environnement virtuel introuvable. Creation en cours...
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)
python -m streamlit run app.py
pause
