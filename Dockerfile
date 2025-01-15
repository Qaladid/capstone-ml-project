FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-cu113.2-6.py39

RUN pipenv install tensorflow==2.10.0

COPY DensNet_v5_06_0.960.keras.tflite . 
COPY cloud_function.py .

CMD ["cloud_function.predict"]



