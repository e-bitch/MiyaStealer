@echo off
pip install -r requirements.txt %*
python builder.py %*
pause
