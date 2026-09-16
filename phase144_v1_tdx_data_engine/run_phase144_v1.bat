@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo Phase144-v1 TDX Data Engine
echo ========================================
echo TDX data path: D:\new_tdx\vipdoc
echo.

where py >nul 2>&1
if %ERRORLEVEL%==0 (
    set "PY=py"
) else (
    where python >nul 2>&1
    if %ERRORLEVEL%==0 (
        set "PY=python"
    ) else (
        echo [ERROR] Python was not found.
        echo Please install Python 3.10 or newer.
        echo.
        pause
        exit /b 1
    )
)

echo Starting Phase144-v1...
echo.
%PY% main.py
set "ERR=%ERRORLEVEL%"

echo.
echo ========================================
if "%ERR%"=="0" (
    echo Completed successfully.
) else (
    echo Program exited with error code %ERR%.
)
echo Report: output\tdx_check_report.txt
echo ========================================
echo.
pause
exit /b %ERR%
