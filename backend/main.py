from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EventRequest, PlannerResponse
from agents import EventPlannerAgents
import uvicorn
import os

app = FastAPI(title="Festiva Planner AI")

# This is the "Door" that lets the frontend in
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows any local connection
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable for agents
planner_agents = None

@app.on_event("startup")
async def startup_event():
    global planner_agents
    try:
        planner_agents = EventPlannerAgents()
        print("✅ Backend Agents Ready!")
    except Exception as e:
        print(f"❌ Error starting agents: {e}")

@app.post("/api/plan", response_model=PlannerResponse)
async def plan_event(request: EventRequest):
    if planner_agents is None:
        return {"error": "Agents not initialized"}
    return planner_agents.plan_event(request)

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)