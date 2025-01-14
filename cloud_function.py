#!/usr/bin/env python
# coding: utf-8

import numpy as np
from PIL import Image
import requests
from io import BytesIO
import tensorflow as tf  # Use tensorflow instead of tflite_runtime


# Function to download the image from the URL
def download_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.convert('RGB')  # Convert to RGB to ensure 3 channels
    img = img.resize((224, 224), Image.NEAREST)  # Resize the image
    return img


# Preprocess the image as expected by the model
def preprocess_input(x):
    x /= 127.5
    x -= 1.
    return x


# Load and process the image
def predict_image_from_url(url):
    # Automatically load the model
    model_path = 'DensNet_v5_06_0.960.keras.tflite'  # You can hardcode your model path here
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    # Download the image from URL
    img = download_image_from_url(url)
    
    # Convert the image to numpy array
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


# Example usage:
url = 'https://github.com/Qaladid/images/raw/master/chest_xray/chest_xray'
