# Use an official Python runtime as a parent image
FROM python:3.11.5-slim-bullseye

# Environment variables to improve performance and behavior
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Install Gunicorn for production server
RUN pip install gunicorn

# Add the project files to the working directory
COPY . /app/

# Collect static files (Whitenoise will handle serving them)
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the application using Gunicorn, ensuring static files are served with Whitenoise
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "magical.wsgi:application"]

