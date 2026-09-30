@echo off
chcp 65001 >nul
rem Take the phones: free them within a minute and stop giving them to Sleepwalker sessions.
cd /d "%~dp0.."
python harness\sw.py stop %*
pause
