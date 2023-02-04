@echo off
python -m pip install -r requirements.txt
python builder.py %*
pause
