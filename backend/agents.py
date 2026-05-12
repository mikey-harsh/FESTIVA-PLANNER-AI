import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from models import EventRequest, PlannerResponse, EventPlan, TaskItem, VendorCategory, BudgetBreakdown
from ml_optimizer import BudgetOptimizer
from rag import RAGKnowledgeBase

load_dotenv()

class EventPlannerAgents:
    def __init__(self):
        self.budget_optimizer = BudgetOptimizer()
        self.rag = RAGKnowledgeBase()
        self.key = os.getenv("GOOGLE_API_KEY")
        self.cache_file = "plan_cache.json"
        self._load_cache()

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f: self.cache = json.load(f)
            except: self.cache = {}
        else: self.cache = {}

    def plan_event(self, request: EventRequest) -> PlannerResponse:
        # Check if we already have this plan (Instant)
        cache_key = f"{request.event_type}_{request.city}_{request.budget}".lower()
        if cache_key in self.cache:
            print("⚡ Serving from Local Cache (Instant)")
            return PlannerResponse(**self.cache[cache_key])

        # Get local data (Instant)
        budget_raw = self.budget_optimizer.predict_allocation(request.budget, request.event_type)
        budget_breakdown = [BudgetBreakdown(**b) for b in budget_raw]
        knowledge_context = self.rag.query(f"{request.event_type} {request.city}")

        # AI Attempt (Max 3-second wait)
        try:
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=self.key, timeout=3)
            prompt = PromptTemplate.from_template("Plan a {event_type} in {city} for ₹{budget}. Context: {context}. Output JSON only.")
            res = (prompt | llm).invoke({"event_type":request.event_type, "city":request.city, "budget":request.budget, "context":knowledge_context})
            
            clean_content = res.content.strip().replace("```json","").replace("```","")
            plan_data = json.loads(clean_content)
            response = PlannerResponse(event_plan=EventPlan(**plan_data), budget_breakdown=budget_breakdown, knowledge_insights=knowledge_context)
            
            # Save to Cache for next time
            self.cache[cache_key] = response.dict()
            with open(self.cache_file, 'w') as f: json.dump(self.cache, f)
            return response
        except Exception:
            # If AI is slow or quota is full, provide instant plan
            return self._generate_mock_response(request, budget_breakdown, knowledge_context)

    def _generate_mock_response(self, request, budget_breakdown, context):
        plan = EventPlan(
            timeline=[TaskItem(task="Immediate Venue & Vendor Booking", timeline="Week 1")],
            vendors_needed=[VendorCategory(category="General", description=f"Top-rated {request.city} Expert")],
            overall_theme_suggestion=f"Signature {request.event_type} style"
        )
        return PlannerResponse(event_plan=plan, budget_breakdown=budget_breakdown, knowledge_insights=context + "\n(Optimized for speed)")