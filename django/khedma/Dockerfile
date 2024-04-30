# Use an official Python runtime as the base image with the desired Python version
FROM python:3.11.4

# Set environment variables to ensure Python outputs are unbuffered
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /django/khedma

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the project's dependencies using the specified Python version
RUN pip install -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "khedma.wsgi", "--bind", "0.0.0.0:8000"]
