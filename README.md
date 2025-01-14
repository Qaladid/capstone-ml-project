# Pneumonia Prediction Model using DenseNet121

#### Pneumonia X-ray Image
![Pneumonia Image](https://github.com/Qaladid/images/raw/master/chest_xray/chest_xray/test/PNEUMONIA/person100_bacteria_477.jpeg)

#### Normal X-ray Image
![Normal Image](https://github.com/Qaladid/images/raw/master/chest_xray/chest_xray/test/NORMAL/IM-0006-0001.jpeg)

## Problem Formulation
The goal of this project is to build an automated tool to assist medical professionals in faster and more accurate diagnosis of respiratory conditions, particularly pneumonia, using machine learning.

The model is trained on a dataset of X-ray images and uses a deep learning architecture (DenseNet121) for the classification of pneumonia. The ultimate aim is to deploy this model in a real-world scenario where it can help healthcare professionals make quick, informed decisions based on radiology images.

## Impact
This project is expected to enhance the diagnostic process for respiratory conditions, improving patient care and reducing the time required for diagnosis. By automating the detection of pneumonia from X-ray images, the tool can significantly aid doctors and radiologists, enabling them to focus more on complex cases and treatment decisions rather than spending excessive time on image interpretation.

## Data Source
The dataset used for training the model is from Kaggle:  
[Pneumonia Prediction Model using VGG16](https://www.kaggle.com/models/huzaifa10/pneumonia-prediction-model-using-vgg16)

## Summary of Steps

1. **Data Preprocessing and Model Training**
   - The model was trained using a DenseNet121 architecture to classify pneumonia in chest X-ray images. Training was conducted in a notebook environment, and the notebook was converted into a Python script after model training.

2. **Dockerization of Python Script**
   - After training the model, the Python script was Dockerized to ensure that the model can be packaged and deployed in a cloud environment consistently.

3. **Google Cloud Function Deployment**
   - The Docker image was deployed as a Google Cloud Function. This allows the model to be hosted in a serverless environment that automatically scales in response to HTTP requests.

---

## How to Run the Project Locally

### 1. **Clone the Repository**

First, clone the repository to your local machine:

```bash
git clone https://github.com/qaladid/capstone-ml-project.git
cd capstone-ml-project 
```

### 2. **Set Up Dependencies**
Install the required Python dependencies using pipenv:

```bash
pipenv install -r requirements.txt
```

### 3. **Build the Docker Image Locally**

To ensure everything works locally, you can build the Docker image on your machine:
```bash
docker build -t pneumonia-prediction .
```

### 4. **Run the Model Locally Using Docker**

After building the image, you can run the model in a Docker container:
```bash
docker run -p 8080:8080 pneumonia-prediction
```
This will run the model locally, and you can test it by sending a request to http://localhost:8080.


### 5. **Test the Local Deployment**

Once the model is running locally, you can test it by sending an image to the prediction endpoint using Postman or cURL.
```bash
curl -X POST http://localhost:8080/predict \
  -F "image=@path_to_image.jpg"
```
The server will return the prediction on whether the image indicates pneumonia or not.


## How to Deploy the Project on Google Cloud Functions

### 1. **Set Up Google Cloud Project**
 - Create a new project on Google Cloud Console and enable the Cloud Functions and Cloud Build APIs.
 - Authenticate your Google Cloud account with the following command:
```bash
gcloud auth login
```

### 2. **Build and Push Docker Image to Google Container Registry**

To push the Docker image to Google Container Registry (GCR):
 - 1. Authenticate Docker with Google Cloud:
 ```bash
 gcloud auth configure-docker
```
 - 2. Build the Docker image:
 ```bash
 docker build -t gcr.io/YOUR_PROJECT_ID/pneumonia-prediction .
```
 - 3. Push the image to GCR:
 ```bash 
 docker push gcr.io/YOUR_PROJECT_ID/pneumonia-prediction
```

### 3. **Deploy to Google Cloud Functions**

Now, deploy the Docker image as a Google Cloud Function using the following command:
```bash
gcloud functions deploy pneumonia-prediction \
  --image gcr.io/YOUR_PROJECT_ID/pneumonia-prediction \
  --region us-central1 \
  --trigger-http \
  --allow-unauthenticated
```

### 4. **Test the Deployment**

Once the function is deployed, you’ll receive a URL from Google Cloud Functions. You can test the function by sending a request to this URL.

Example cURL command:
```bash
curl -X POST https://your-app-name-xyz.a.run.app/predict \
  -F "image=@path_to_image.jpg"
```

## Future Improvements

 - Enhance the model with additional data and fine-tuning to improve its accuracy.
 - Implement real-time monitoring and logging for better performance tracking.
 - Optimize the deployment with auto-scaling and serverless configurations.
 - Add user authentication and more robust error handling in the Cloud Function.