# Use an official Python runtime as a parent image
# python:3.10-slim is a great choice as a slim base image.
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# The following RUN command updates and upgrades the base image's packages
# to their latest, most secure versions to patch known vulnerabilities.
# This is a critical step for reducing high- and medium-severity issues.
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
