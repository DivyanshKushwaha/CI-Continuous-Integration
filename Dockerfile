# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port your Flask app runs on (default is 5000)
EXPOSE 5000

# Copy the rest of the application
COPY . /app/

# Define the default command to run the Flask app
CMD ["python", "app.py"]
