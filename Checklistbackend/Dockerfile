# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Checklistbackend.settings

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver"]
