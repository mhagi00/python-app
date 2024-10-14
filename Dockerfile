# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask mysql-connector-python

# Expose the port that Flask will listen on
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
