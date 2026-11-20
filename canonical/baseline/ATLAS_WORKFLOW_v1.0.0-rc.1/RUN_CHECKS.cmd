@echo off
cd /d "%~dp0"
py -3 RUN_CHECKS.py
if errorlevel 1 pause
