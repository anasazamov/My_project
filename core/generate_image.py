import requests
import json
import shutil


def download_image(url, file_name):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(file_name, 'wb') as file:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file) 
        
    return open("image.jp","rb")


def get_result(data):
    url = "https://api.midjourneyapi.io/result"

    payload = json.dumps({
    "resultId": data
    })
    headers = {
    'Authorization': 'd1b9e9b9-89e8-48dd-b12c-6818e0c360be',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()["imageURL"]


image_url = get_result()
file_name = 'image.jpg'
download_image(image_url, file_name)

def get_json(description: str):
    url = "https://api.midjourneyapi.io/imagine"
    mid_token='d1b9e9b9-89e8-48dd-b12c-6818e0c360be'
    payload = json.dumps({
    "prompt": description,
    "callbackURL": "azamovanas.pythonanywhere.com/mid"
    })
    headers = {
    'Authorization': mid_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    return download_image(get_result(response.json()["resultId"]),"image.jpg")


