**[Live Demo: Festiva Planner AI](https://festiva-planner-ai-ui-production.up.railway.app)**

---

# 🚀 Festiva Planner AI: Intelligence-Driven Event Strategy

**Festiva Planner AI** is a modern, full-stack AI application designed to revolutionize event planning. By combining **Machine Learning** for budget optimization, **RAG (Retrieval-Augmented Generation)** for expert domain knowledge, and **Multi-Agent Orchestration**, it provides users with an instant, actionable event roadmap.

---

## 🧠 Core Intelligence Features

* **ML-Powered Budget Intelligence:** Uses a `RandomForestRegressor` model to predict optimal cost allocation across five key categories based on event type and total budget.
* **Local RAG Engine:** Implements a high-speed, 100% local Knowledge Base using `TF-IDF` vectorization to provide expert planning insights without API latency.
* **Multi-Agent Coordination:** Features a "Lead Architect" and "Financial Strategist" agent logic with smart 3-second timeouts and high-fidelity mock fallbacks.
* **Intelligent Caching:** Implements local JSON-based persistent caching to ensure 0ms response times for repeat queries.

---

## 🛠️ Technical Stack

* **Frontend:** React (Vite), Tailwind CSS, Lucide Icons, Framer Motion
* **Backend:** FastAPI (Python), Uvicorn
* **AI/ML:** Scikit-learn, LangChain, Google Gemini 2.0 Flash
* **Vector Search:** TF-IDF + Cosine Similarity (Custom Local Implementation)
* **Deployment:** Docker, Railway

---

## 🎨 Modern Aesthetic UI

The application features a premium "Night Owl" theme with:
* **Glassmorphism Panels:** Sophisticated backdrop filters for a professional look.
* **Zero-Whitespace PDF Export:** High-quality client-side report generation using `jsPDF` and `html2canvas`.
* **Responsive Wizard:** A clean, centered multi-input form designed for high-conversion UX.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* Node.js 18+
* Google Gemini API Key

### Backend Setup
1. `cd backend`
2. `python -m venv venv`
3. `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. `pip install -r requirements.txt`
5. Create a `.env` file with `GOOGLE_API_KEY="your_key_here"`
6. `python main.py`

### Frontend Setup
1. `cd frontend`
2. `npm install`
3. `npm run dev`

---

## 📈 Engineering Highlights

* **Latency Optimization:** Reduced AI response wait time from 20s to <1s through hybrid caching and local RAG.
* **Robustness:** Implemented a non-breaking error-handling system that maintains UI integrity during API rate-limiting events.
* **Security:** Configured `.gitignore` to prevent leakage of sensitive `.env` data and environment-specific artifacts.
