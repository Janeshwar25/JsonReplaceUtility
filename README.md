@echo off
setlocal

cd /d "%~dp0"

echo ========================================
echo JsonReplaceUtility Started
echo Date: %date%
echo Time: %time%
echo ========================================

python "%~dp0replace_json.py" %*

set "EXITCODE=%ERRORLEVEL%"

echo.
echo Python Exit Code: %EXITCODE%

if not "%EXITCODE%"=="0" (
    echo FAILED - Python exited with code %EXITCODE%.
    exit /b %EXITCODE%
)

echo Python completed successfully.
echo Copying updated.json to ACCELQ user_data...

copy /Y "%~dp0output\updated.json" "C:\Users\jchowdha\ACCELQAgent_1\AgentInstances\agent\user_data\updated.json"

if errorlevel 1 (
    echo FAILED - Could not copy updated.json
    exit /b 1
)

echo SUCCESS - updated.json copied to ACCELQ user_data.
echo ========================================

endlocal
exit /b 0
