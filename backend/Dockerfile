FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# We ONLY pre-bake the ML model because it does not need an API key.
# We removed the RAG line because it requires an API key to initialize.
RUN python -c "from ml_optimizer import BudgetOptimizer; BudgetOptimizer()"

# Expose port
EXPOSE 8000

# Start server using the PORT environment variable provided by Render
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"