# Use an official Python runtime as the base image with the desired Python version
FROM python:3.11.4

# Set environment variable to ensure Python outputs are unbuffered
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /django/khedma

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the project's dependencies using the specified Python version
RUN pip install -r requirements.txt

####
# Copy the rest of your project files into the container
COPY . .



# Make migrations
#RUN python3 manage.py makemigrations

#RUN python manage.py collectstatic --noinput

# Apply migrations
# RUN python3 manage.py migrate 
CMD ["./wait-for-it.sh", "database:5432", "--", "python", "manage.py", "migrate"]


# CMD python3 manage.py runserver 0.0.0.0:$PORT


