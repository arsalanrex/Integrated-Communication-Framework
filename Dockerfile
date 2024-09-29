# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /Integrated-Communication-Framework

# Copy the current directory contents into the container
COPY . /Integrated-Communication-Framework

# Install any necessary Python packages (from requirements.txt if available)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Install python-dotenv to manage .env files
RUN pip install python-dotenv
# Expose the port the app runs on
EXPOSE 8081
# Run the init_db.py script first
CMD ["sh", "-c", "python init_db.py && python smtp_server.py && python app.py"]
