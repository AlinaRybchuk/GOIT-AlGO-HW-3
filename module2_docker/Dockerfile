# Use an official Python runtime as a parent image
FROM python:3.8.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock* /app/
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install poetry

# Install dependencies using Poetry
RUN poetry install

# Copy the rest of the application code to the container
COPY . /app

# Let's run our application inside the container
ENTRYPOINT ["poetry", "run", "python", "app.py"]

# Indicate the port where the application works inside the container
EXPOSE 8080




