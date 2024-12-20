# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY web_app-container.py /app/
COPY requirements.txt /app/
COPY templates /app/templates
COPY static /app/static

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5001

# Command to run the application
CMD ["python", "web_app-container.py"]
