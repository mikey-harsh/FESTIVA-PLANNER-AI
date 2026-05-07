from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EventRequest, PlannerResponse
from agents import EventPlannerAgents
import uvicorn
import os

app = FastAPI(title="Festiva Planner AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://festiva-planner-ai-ui.onrender.com", # Your live frontend
        "http://localhost:5173",                     # Local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable for lazy loading
planner_agents = None

def get_planner():
    global planner_agents
    if planner_agents is None:
        planner_agents = EventPlannerAgents()
    return planner_agents

@app.post("/api/plan", response_model=PlannerResponse)
async def plan_event(request: EventRequest):
    # Initialize agents only when the first request hits
    agents = get_planner()
    response = agents.plan_event(request)
    return response

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    # Use the PORT environment variable if provided by Render
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)