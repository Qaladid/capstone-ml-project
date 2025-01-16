FROM tensorflow/tensorflow:2.10.0-gpu

WORKDIR /app

# Copy your requirements.txt file
COPY requirements.txt .

# Install pipenv and install dependencies
RUN pip install pipenv && pipenv install --dev

# Copy the model and the cloud function code
COPY DensNet_v5_06_0.960.keras.tflite .
COPY cloud_function.py .

# Expose port 8080, which Cloud Run uses by default
EXPOSE 8080

# Set the default command to run the Python script
CMD ["pipenv", "run", "python", "cloud_function.py"]
