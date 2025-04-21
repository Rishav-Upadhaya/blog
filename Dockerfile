# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory for subsequent commands
WORKDIR /app

# Update pip to latest version
RUN pip install --upgrade pip 

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files into container
COPY . /app/

# Specify port the application will listen on
EXPOSE 8000

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]