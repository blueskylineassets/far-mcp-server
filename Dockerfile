# FAR MCP Server Dockerfile
# Lightweight container for running the MCP server

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first (for better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py client.py ./

# Environment variables (should be provided at runtime)
# RAPIDAPI_KEY must be set when running the container

# Run the MCP server in stdio mode
# Note: For Docker usage, you may need to configure stdio properly
# or use a different transport (e.g., SSE)
ENTRYPOINT ["python", "server.py"]

