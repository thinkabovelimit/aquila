# Use lightweight Python base
FROM python:3.11-slim

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential libnuma1 libnuma-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install smallpond
RUN pip install --no-cache-dir smallpond

# Copy entrypoint script
COPY entrypoint.py /app/entrypoint.py
COPY prices.parquet /app/prices.parquet

# Run the script by default
CMD ["python", "entrypoint.py"]
