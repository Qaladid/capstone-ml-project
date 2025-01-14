# Pneumonia Prediction Model using VGG16

## Problem Formulation
The goal of this project is to build an automated tool to assist medical professionals in faster and more accurate diagnosis of respiratory conditions, particularly pneumonia, using machine learning.

The model is trained on a dataset of X-ray images and uses a deep learning architecture (VGG16) for the classification of pneumonia. The ultimate aim is to deploy this model in a real-world scenario where it can help healthcare professionals make quick, informed decisions based on radiology images.

## Impact
This project is expected to enhance the diagnostic process for respiratory conditions, improving patient care and reducing the time required for diagnosis. By automating the detection of pneumonia from X-ray images, the tool can significantly aid doctors and radiologists, enabling them to focus more on complex cases and treatment decisions rather than spending excessive time on image interpretation.

## Data Source
The dataset used for training the model is from Kaggle:  
[Pneumonia Prediction Model using VGG16](https://www.kaggle.com/models/huzaifa10/pneumonia-prediction-model-using-vgg16)

## Summary of Steps

1. **Data Preprocessing and Model Training**
   - The model was trained using a VGG16 architecture to classify pneumonia in chest X-ray images. The training was conducted in a notebook environment on Saturn Cloud.
   
2. **Flask API Development**
   - After training the model, a Flask API was developed to serve the trained model for inference. This API allows users to send X-ray images and receive predictions on whether the image indicates pneumonia.

3. **Dockerization of Flask API**
   - To ensure that the model and API can be deployed consistently across different environments, the Flask API was Dockerized using a custom Dockerfile. This step prepares the application for deployment.

4. **Local Testing**
   - The Flask app was tested locally by running it inside a Docker container to ensure that it works correctly before proceeding with the deployment to cloud platforms.

5. **Azure Function App Preparation**
   - The application was then prepared for deployment as an Azure Function App using a custom Docker container, allowing easy scaling and management in the cloud.

6. **Pushing Docker Image to Azure Container Registry (ACR)**
   - The Docker image was pushed to the Azure Container Registry, enabling it to be pulled and deployed to the Azure platform.

7. **Google Cloud Function Deployment**
   - As a final step, the Docker image was deployed to Google Cloud Functions, which provides a serverless solution for executing code in the cloud in response to HTTP requests.

8. **Testing and Monitoring**
   - Once deployed, the cloud functions were tested and monitored to ensure the application is functioning properly and providing accurate predictions.

## Future Improvements
- Enha
