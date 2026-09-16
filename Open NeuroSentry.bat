@echo off
setlocal

set "PROJECT_DIR=%~dp0"
set "PYTHON=%PROJECT_DIR%venv\Scripts\python.exe"

if not exist "%PYTHON%" (
  echo NeuroSentry Python environment was not found:
  echo %PYTHON%
  pause
  exit /b 1
)

start "NeuroSentry API" /D "%PROJECT_DIR%" cmd /k ""%PYTHON%" -m uvicorn app:app --host 127.0.0.1 --port 8000"
start "NeuroSentry Frontend" /D "%PROJECT_DIR%" cmd /k "npm.cmd run dev"

timeout /t 8 /nobreak >nul
start "" "http://localhost:3000"

echo NeuroSentry is opening at http://localhost:3000
echo Keep the two server windows open during your presentation.
endlocal
