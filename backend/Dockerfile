# backend/Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file if it exists, otherwise create a basic one
COPY requirements.txt* ./

# If requirements.txt doesn't exist, install basic Django and psycopg2
RUN if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    else \
        pip install --no-cache-dir django psycopg2-binary python-dotenv; \
    fi

# Copy project
COPY . .

# Create necessary directories
RUN mkdir -p staticfiles media

# Expose port
EXPOSE 8100

# Run migrations and start server (you can customize this)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8100"]