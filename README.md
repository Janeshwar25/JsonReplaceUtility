@echo off
setlocal

cd /d "%~dp0"

echo Starting Validator API on port 5001...
echo.

python validator_api.py

echo.
echo Validator API stopped.
pause
