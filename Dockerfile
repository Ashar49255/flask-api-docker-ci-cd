# Base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Set environment variable for Python path
ENV PYTHONPATH=/app

# Copy requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the project files into the container
COPY . .

# Expose Flask's default port
EXPOSE 5000

# Run the Flask application
CMD ["python", "run.py"]
