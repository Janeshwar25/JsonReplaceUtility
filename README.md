@echo off
setlocal

REM Go to JsonReplaceUtility folder
cd /d "%~dp0"

echo ========================================
echo JsonReplaceUtility Started
echo Date: %date%
echo Time: %time%
echo Folder: %CD%
echo ========================================

REM Run Python utility
python "%~dp0replace_json.py" %*

set "EXITCODE=%ERRORLEVEL%"

echo.
echo Python Exit Code: %EXITCODE%

REM Check whether updated.json was generated
if exist "%~dp0updated.json" (
    echo updated.json found.

    copy /Y "%~dp0updated.json" "C:\Users\jchowdha\ACCELQAgent_1\Agents\instances\agent\user_data\updated.json"

    if errorlevel 1 (
        echo FAILED - Could not copy updated.json
        set "EXITCODE=1"
    ) else (
        echo SUCCESS - updated.json copied successfully.
    )
) else (
    echo FAILED - updated.json was NOT generated.
    set "EXITCODE=1"
)

echo.
echo Final Exit Code: %EXITCODE%
echo ========================================

endlocal & exit /b %EXITCODE%
