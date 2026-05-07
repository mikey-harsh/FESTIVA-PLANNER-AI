FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
# (Removed build-essential to drastically speed up Render build times, as pip provides pre-compiled wheels for our packages)

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# CRITICAL FIX: Pre-download the HuggingFace model and pre-build the FAISS/ML models 
# DURING the Docker build phase, so the server starts instantly at runtime!
RUN python -c "from langchain_community.embeddings import HuggingFaceEmbeddings; HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')"
RUN python -c "from ml_optimizer import BudgetOptimizer; BudgetOptimizer()"
RUN python -c "from rag import RAGKnowledgeBase; RAGKnowledgeBase()"

# Expose port
EXPOSE 8000

# Start server
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
