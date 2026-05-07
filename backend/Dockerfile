FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
# (Removed build-essential to drastically speed up Render build times, as pip provides pre-compiled wheels for our packages)

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Expose port
EXPOSE 8000

# Start server
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
