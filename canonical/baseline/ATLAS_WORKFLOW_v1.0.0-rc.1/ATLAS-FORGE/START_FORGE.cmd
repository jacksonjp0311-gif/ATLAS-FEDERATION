@echo off
setlocal
cd /d "%~dp0"
set "PYTHONPATH=%~dp0src"
py -3 -m atlas_forge serve
if errorlevel 1 pause
