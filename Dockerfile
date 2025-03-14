# Use an official Python runtime as a parent image
FROM  python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]
