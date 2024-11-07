# Use the official Python image from the Docker Hub
FROM python:3.12.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE backend.settings

# Set the working directory
WORKDIR /../backend

# Install dependencies
COPY requirements.txt /../backend/
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files
COPY . /../backend/

# Expose the port on which the app will run
EXPOSE 8000

# Run migrations and collect static files
RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Run the Gunicorn server
CMD ["gunicorn", "--config", "gunicorn_config.py", "backend.wsgi:application"]