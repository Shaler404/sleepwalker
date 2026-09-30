@echo off
chcp 65001 >nul
rem Вернуть телефоны в работу Sleepwalker.
cd /d "%~dp0.."
python harness\sw.py resume %*
pause
