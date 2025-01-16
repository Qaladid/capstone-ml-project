import requests
import json

# Simulate a request to your prediction API
def test_prediction(url):
    response = requests.post("http://localhost:8080", json={"url": url})
    if response.status_code == 200:
        print(f"Prediction: {response.text}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    test_url = "https://raw.githubusercontent.com/Qaladid/images/master/chest_xray/chest_xray/test/PNEUMONIA/person100_bacteria_477.jpeg"
    test_prediction(test_url)
