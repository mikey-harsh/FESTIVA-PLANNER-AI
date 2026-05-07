FROM python:3.10-slim

WORKDIR /app

# Install dependencies required for FAISS and compiling C++ extensions
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Expose port
EXPOSE 8000

# Start server
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
