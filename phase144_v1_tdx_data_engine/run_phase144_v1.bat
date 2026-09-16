@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ========================================
echo Phase144-v1 TDX Data Engine
echo TDX: D:\new_tdx\vipdoc
echo ========================================
echo.
python main.py
set ERR=%ERRORLEVEL%
echo.
if not "%ERR%"=="0" echo 运行失败，错误码：%ERR%
echo 报告位置：output\tdx_check_report.txt
pause
exit /b %ERR%
