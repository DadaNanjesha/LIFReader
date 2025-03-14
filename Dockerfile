# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]
