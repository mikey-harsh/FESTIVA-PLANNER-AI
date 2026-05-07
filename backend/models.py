from pydantic import BaseModel
from typing import List, Optional, Dict

class EventRequest(BaseModel):
    event_type: str  # e.g., "Wedding", "Corporate", "Birthday"
    budget: float    # e.g., 1000000 (10 Lakhs)
    city: str        # e.g., "Bangalore"
    preferences: str # e.g., "Outdoor, evening, 500 guests, vegetarian"

class TaskItem(BaseModel):
    task: str
    timeline: str    # e.g., "Month 1", "Week 1", "Day of Event"

class VendorCategory(BaseModel):
    category: str    # e.g., "Catering", "Venue", "Photography"
    description: str # Brief description of what to look for

class EventPlan(BaseModel):
    timeline: List[TaskItem]
    vendors_needed: List[VendorCategory]
    overall_theme_suggestion: str

class BudgetBreakdown(BaseModel):
    category: str
    allocated_amount: float
    percentage: float

class PlannerResponse(BaseModel):
    event_plan: EventPlan
    budget_breakdown: List[BudgetBreakdown]
    knowledge_insights: str  # Any insights from RAG
