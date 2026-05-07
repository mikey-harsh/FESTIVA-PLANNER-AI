from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EventRequest, PlannerResponse
from agents import EventPlannerAgents
import uvicorn

app = FastAPI(title="Festiva Planner AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For dev purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

planner_agents = EventPlannerAgents()

@app.post("/api/plan", response_model=PlannerResponse)
async def plan_event(request: EventRequest):
    response = planner_agents.plan_event(request)
    return response

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
