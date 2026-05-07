import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import json

from models import EventRequest, PlannerResponse, EventPlan, TaskItem, VendorCategory, BudgetBreakdown
from ml_optimizer import BudgetOptimizer
from rag import RAGKnowledgeBase

load_dotenv()

class EventPlannerAgents:
    def __init__(self):
        self.llm = self._get_llm()
        self.budget_optimizer = BudgetOptimizer()
        self.rag = RAGKnowledgeBase()

    def _get_llm(self):
        if os.getenv("GOOGLE_API_KEY"):
            return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)
        elif os.getenv("OPENAI_API_KEY"):
            return ChatOpenAI(model="gpt-4o", temperature=0.7)
        else:
            # Fallback mock if no API key is provided
            return None

    def plan_event(self, request: EventRequest) -> PlannerResponse:
        # 1. Knowledge Agent -> Get context from RAG
        query = f"What are the best practices and timeline for planning a {request.event_type} event?"
        knowledge_context = self.rag.query(query)

        # 2. Budget Agent -> Get ML allocation
        budget_breakdown_raw = self.budget_optimizer.predict_allocation(request.budget, request.event_type)
        budget_breakdown = [BudgetBreakdown(**b) for b in budget_breakdown_raw]

        # 3. Planner Agent -> Generate timeline and vendor list
        if self.llm is None:
            # Mock response if no LLM
            plan = EventPlan(
                timeline=[
                    TaskItem(task="Book Venue (Mandapam/Banquet)", timeline="Month 1"),
                    TaskItem(task="Finalize Catering Menu", timeline="Month 2"),
                    TaskItem(task="Book Decorator & Photographer", timeline="Month 3"),
                    TaskItem(task="Send out Invitations", timeline="Month 4")
                ],
                vendors_needed=[
                    VendorCategory(category="Venue", description=f"The Grand Imperial Banquet, {request.city} - Spacious, premium feel (approx. ₹1500/plate)"),
                    VendorCategory(category="Catering", description=f"Shree Krishna Caterers, {request.city} - Authentic multi-cuisine and live counters"),
                    VendorCategory(category="Photography", description=f"Cinematic Moments Studio, {request.city} - Traditional & Candid coverage"),
                    VendorCategory(category="Decor", description=f"Royal Petals Decorators, {request.city} - Premium floral mandap/stage setup")
                ],
                overall_theme_suggestion="Royal Indian Heritage"
            )
            return PlannerResponse(
                event_plan=plan,
                budget_breakdown=budget_breakdown,
                knowledge_insights=knowledge_context + "\n\n[Note: Used Mock LLM as no GOOGLE_API_KEY or OPENAI_API_KEY was found in .env]"
            )

        # Prompt for LLM
        prompt = PromptTemplate.from_template(
            """You are an expert event planner AI.
            Plan a {event_type} event in {city} (India) with a budget of ₹{budget}.
            User preferences: {preferences}.
            
            Knowledge Base Context (Indian Vendors & Guidelines):
            {knowledge_context}
            
            CRITICAL INSTRUCTION: Based on the city ({city}), you MUST recommend specific, realistic Indian vendor names from the context provided. If the specific city is not in the context, INVENT highly realistic local Indian vendor names for {city} (e.g., 'Royal Banquet', 'A1 Caterers', 'Vivid Clicks').
            DO NOT just say 'Caterer needed'. You MUST say something like 'Caterer: Spice Route Catering - Multi-cuisine buffet'.
            
            Please provide a structured event plan. The output must be valid JSON with this structure:
            {{
                "timeline": [
                    {{"task": "task description", "timeline": "timeframe"}}
                ],
                "vendors_needed": [
                    {{"category": "vendor category", "description": "Specific Vendor Name - what they provide and estimated cost"}}
                ],
                "overall_theme_suggestion": "theme suggestion"
            }}
            
            Only output the JSON object, nothing else. Do not wrap in markdown tags.
            """
        )
        
        chain = prompt | self.llm
        response = chain.invoke({
            "event_type": request.event_type,
            "city": request.city,
            "budget": request.budget,
            "preferences": request.preferences,
            "knowledge_context": knowledge_context
        })
        
        # Clean response and parse JSON
        try:
            content = response.content if hasattr(response, 'content') else str(response)
            content = content.strip()
            if content.startswith("```json"):
                content = content.split("```json")[1].split("```")[0].strip()
            elif content.startswith("```"):
                content = content.split("```")[1].split("```")[0].strip()
                
            plan_data = json.loads(content)
            plan = EventPlan(**plan_data)
        except Exception as e:
            # Fallback if parsing fails
            plan = EventPlan(
                timeline=[TaskItem(task="Parsing error, fallback timeline", timeline="N/A")],
                vendors_needed=[],
                overall_theme_suggestion="Error generating theme"
            )
            
        return PlannerResponse(
            event_plan=plan,
            budget_breakdown=budget_breakdown,
            knowledge_insights=knowledge_context
        )
