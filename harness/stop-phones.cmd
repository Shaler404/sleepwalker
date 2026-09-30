@echo off
chcp 65001 >nul
rem Забрать телефоны: за минуту освободить и не выдавать сессиям Sleepwalker.
cd /d "%~dp0.."
python harness\sw.py stop %*
pause
