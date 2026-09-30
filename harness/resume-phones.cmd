@echo off
chcp 65001 >nul
rem Return the phones to Sleepwalker work.
cd /d "%~dp0.."
python harness\sw.py resume %*
pause
