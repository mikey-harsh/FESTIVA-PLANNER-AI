@echo off
echo Starting Festiva Planner AI Backend...
start cmd /k "cd backend && .\venv\Scripts\activate.bat && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

echo Starting Festiva Planner AI Frontend...
start cmd /k "cd frontend && npm run dev"

echo Servers are starting up!
echo Backend API will be at: http://localhost:8000
echo Frontend UI will be at: http://localhost:5173 (usually)
