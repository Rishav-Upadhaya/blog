# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Copy project files into container
COPY . /app

# Set working directory for subsequent commands
WORKDIR /app

# Update pip to latest version
RUN pip install --upgrade pip 

# Install project dependencies
RUN pip install -r requirements.txt

# Create database tables
RUN python manage.py makemigrations
RUN python manage.py migrate

# Specify port the application will listen on
EXPOSE 8000

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]