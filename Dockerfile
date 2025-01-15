FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-cu113.2-6.py39

WORKDIR /app

COPY requirements.txt .

RUN pip install pipenv && pipenv install --no-cache-dir -r requirements.txt


COPY DensNet_v5_06_0.960.keras.tflite . 
COPY cloud_function.py .

CMD ["cloud_function.predict"]



