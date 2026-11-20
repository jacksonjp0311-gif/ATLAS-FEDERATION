@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo Python 3.10 or newer is required. Install it and retry.
  exit /b 2
)
py -3 tools\run_candidate_checks.py
if errorlevel 1 exit /b 2
echo.
echo Local checks completed. Final v1 gates may still be open.
py -3 tools\v1_readiness.py --require-final
exit /b %errorlevel%
