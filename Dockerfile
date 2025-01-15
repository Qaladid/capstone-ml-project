FROM tensorflow/tensorflow:2.10.0-gpu

WORKDIR /app

COPY requirements.txt .

RUN pip install pipenv && pipenv install --no-cache-dir -r requirements.txt


COPY DensNet_v5_06_0.960.keras.tflite . 
COPY cloud_function.py .

CMD ["cloud_function.predict"]



