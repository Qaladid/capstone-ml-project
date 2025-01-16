FROM tensorflow/tensorflow:2.10.0-gpu

WORKDIR /app

# Copy your requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the model and the cloud function code
COPY DensNet_v5_06_0.960.keras.tflite .
COPY cloud_function.py .

# Expose the required port (8080)
EXPOSE 8080

# Set the default command to run the Python script
CMD ["python", "cloud_function.py"]
