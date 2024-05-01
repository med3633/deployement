# FROM python:3.11.4
# # directory of working
# WORKDIR /django/khedma
# # # Copy the requirements.txt file into the container
# COPY requirements.txt requirements.txt

# # # Install the project's dependencies using the specified Python version
# RUN pip install -r requirements.txt

# # ####
# # # Copy the rest of your project files into the container
# COPY . .
# #copy bash file in racine
# COPY ./entrypoint.sh /
# #excute the bash script
# ENTRYPOINT ["sh", "./entrypoint.sh"]




# Use an official Python runtime as the base image with the desired Python version
FROM python:3.11.4

# Set environment variables to ensure Python outputs are unbuffered and doesn't write bytecode
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

# Make migrations (Optional: Only needed if there are changes in models)
# RUN python manage.py makemigrations

# Apply migrations (Required: Apply migrations to the database)

# Collect static files (Optional: Only needed for serving static files)
RUN python manage.py collectstatic --noinput

# Command to run when the container is launched
CMD ["./wait-for-it.sh", "database:5432", "--", "python", "manage.py", "migrate"]
