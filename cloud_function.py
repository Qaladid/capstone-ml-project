#!/usr/bin/env python
# coding: utf-8

import numpy as np
import json
from PIL import Image
import requests
from io import BytesIO
import tensorflow as tf

# Function to download the image from the URL
def download_image_from_url(url):
    response = requests.get(url)
    
    # Check if the URL actually returns an image
    if 'image' not in response.headers['Content-Type']:
        raise ValueError(f"URL did not return an image file. Content-Type: {response.headers['Content-Type']}")
    
    # Open the image
    img = Image.open(BytesIO(response.content))
    img = img.convert('RGB')  # Convert to RGB to ensure 3 channels
    img = img.resize((224, 224), Image.NEAREST)  # Resize the image to match the model input
    return img


# Preprocess the image as expected by the model
def preprocess_input(x):
    x /= 127.5
    x -= 1.  # Normalize image to be between -1 and 1
    return x


# Load and process the image
def predict_image_from_url(url):
    model_path = 'DensNet_v5_06_0.960.keras.tflite'  # You can hardcode your model path here
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    # Download the image from URL
    img = download_image_from_url(url)
    
    # Convert the image to a numpy array
    x = np.array(img, dtype='float32')
    X = np.array([x])
    
    # Preprocess the image
    X = preprocess_input(X)
    
    # Get input and output tensor details
    input_index = interpreter.get_input_details()[0]['index']
    output_index = interpreter.get_output_details()[0]['index']
    
    # Run inference
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    
    # Extract the probability
    probability = preds[0][0]  # Assuming binary classification
    
    # Decode the probability to a binary label
    binary_label = int(probability > 0.5)
    
    # Map binary labels to class names
    class_labels = {0: 'NORMAL', 1: 'PNEUMONIA'}
    predicted_class = class_labels[binary_label]
    
    # Return the result
    return predicted_class, probability


# Cloud Function handler without Flask
def predict(request):
    # Get URL from the request query parameters
    url = request.args.get('url')
    
    if not url:
        return json.dumps({"error": "URL is required"}), 400  # Return error as JSON response
    
    # Call the prediction function
    result = predict_image_from_url(url)
    
    # Return the result in JSON format
    return json.dumps({
        "prediction": result[0],
        "probability": result[1]
    })


