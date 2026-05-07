FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Pre-build only light components. 
#  using Cloud Embeddings.
RUN python -c "from ml_optimizer import BudgetOptimizer; BudgetOptimizer()"
RUN python -c "from rag import RAGKnowledgeBase; RAGKnowledgeBase()"

# Expose port
EXPOSE 8000

# Start server using the PORT environment variable provided by Render
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"