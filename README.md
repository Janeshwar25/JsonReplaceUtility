@echo off
setlocal

echo ========================================
echo JSON REPLACE UTILITY TEST
echo ========================================

echo Current folder:
cd
echo.

echo Moving to utility folder...
cd /d "%~dp0"

echo Now folder is:
cd
echo.

echo Checking Python...
python --version
echo Python error code: %ERRORLEVEL%
echo.

echo Checking replace_json.py...
if exist "%~dp0replace_json.py" (
    echo replace_json.py FOUND
) else (
    echo ERROR: replace_json.py NOT FOUND
)

echo.
echo ========================================
echo Starting Python utility...
echo ========================================

python "%~dp0replace_json.py" %*

echo.
echo ========================================
echo Python finished.
echo Exit Code: %ERRORLEVEL%
echo ========================================

pause
