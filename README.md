
@echo off
setlocal
cd /d "%~dp0"

REM Keep project root importable for Python
set "PYTHONPATH=%~dp0;%PYTHONPATH%"

REM Run the existing JSON utility
python "%~dp0replace_json.py" %*
set "EXITCODE=%ERRORLEVEL%"

echo.
if not "%EXITCODE%"=="0" (
    echo FAILED - Utility exit code %EXITCODE%.
    endlocal & exit /b %EXITCODE%
)

echo SUCCESS - Utility completed.

REM Copy generated JSON to ACCELQ agent user_data
set "SOURCE=%~dp0output\updated.json"
set "TARGET=C:\Users\jchowdha\ACCELQAgent_1\AgentInstances\agent\user_data\updated.json"

if not exist "%SOURCE%" (
    echo ERROR - Generated JSON not found: "%SOURCE%"
    endlocal & exit /b 1
)

if not exist "%TARGET%" (
    echo ERROR - ACCELQ destination file not found: "%TARGET%"
    endlocal & exit /b 1
)

copy /Y "%SOURCE%" "%TARGET%" >nul
if errorlevel 1 (
    echo ERROR - Failed to copy JSON to ACCELQ.
    endlocal & exit /b 1
)

fc /b "%SOURCE%" "%TARGET%" >nul
if errorlevel 1 (
    echo ERROR - JSON copy verification failed.
    endlocal & exit /b 1
)

echo SUCCESS - Latest JSON copied and verified in ACCELQ user_data.
echo.
endlocal & exit /b 0
