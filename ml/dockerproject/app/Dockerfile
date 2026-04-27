# Step 1: Use base image
#FROM python:3.10-slim
FROM python:3.13

# Step 2: Set environment variables (best practice)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set working directory
WORKDIR /app

# Step 4: Install system dependencies (optional but useful)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Copy requirements first (for caching)
COPY requirements.txt .

# Step 6: Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Step 7: Copy application code
COPY . .

# Step 8: Expose port
EXPOSE 5000

# Step 9: Run the application
CMD ["python", "app.py"]