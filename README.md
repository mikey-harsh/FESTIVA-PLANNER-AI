# 🎉 Festiva Planner AI

An intelligent, multi-agent AI event planning assistant powered by Machine Learning and Large Language Models. 

Festiva Planner AI takes the stress out of event planning. Simply input your event type, budget, city, and preferences, and our orchestrated LangChain agents will generate a comprehensive timeline, an optimized budget breakdown, and realistic local vendor recommendations tailored specifically for Indian cities!

---

## ✨ Features

- **Multi-Agent Architecture:** Utilizes LangChain to coordinate a Planner Agent, Budget Agent, and Knowledge Agent.
- **Machine Learning Budget Optimizer:** A custom `scikit-learn` Random Forest model automatically learns and predicts the optimal budget allocation (Venue, Food, Decor, etc.) based on your event type and total budget.
- **RAG Knowledge Base:** Powered by FAISS and HuggingFace Embeddings, the system references a massive local vector database of Indian vendors and event planning guides to ensure highly localized and realistic recommendations.
- **Extensive Event Support:** Supports over 20 event types including Weddings, Corporate Conferences, Baby Showers, and Charity Galas.
- **Aesthetic UI:** A premium, glassmorphic React frontend built with Vite, featuring dynamic progress bars and smooth micro-animations.

---

## 🛠️ Tech Stack

- **Frontend:** React, Vite, Vanilla CSS
- **Backend:** FastAPI, Python
- **AI & ML:** LangChain, Scikit-learn, Pandas, FAISS, HuggingFace (`sentence-transformers`)
- **Deployment:** Docker, Docker Compose

---

## 🚀 How to Run Locally (Easiest Way)

You don't need any complex setup to run this locally on Windows!

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mikey-harsh/FESTIVA-PLANNER-AI.git
   cd FESTIVA-PLANNER-AI
   ```
2. **Add your API Key (Optional):**
   Create a `.env` file in the `backend/` folder and add your key if you want live AI generation (otherwise, it uses a robust offline mock generator):
   ```env
   GOOGLE_API_KEY="your_gemini_key_here"
   # or OPENAI_API_KEY="your_openai_key_here"
   ```
3. **Run the batch script:**
   Simply double-click the `run.bat` file in the root directory. It will automatically install all dependencies, build the ML models, and start both the backend and frontend servers.
4. **View the App:**
   Open your browser and navigate to `http://localhost:5173`.

---

## 🐳 How to Run with Docker

For a production-ready environment, you can spin up the entire application using Docker.

```bash
# Build and start the containers
docker-compose up --build
```
- The frontend will be available at `http://localhost:5173`
- The backend API will be available at `http://localhost:8000`

---


