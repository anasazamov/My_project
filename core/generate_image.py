import requests
import json
import shutil
import core 
import time
from telegram import Update
from telegram.ext import CallbackContext

db=core.DB()

def download_image(url, file_name):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(file_name, 'wb') as file:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file) 
        
    return open("image.jpg","rb")


def get_result(data,a,b,callback: Update,bot:CallbackContext):
    
        
    url = "https://api.midjourneyapi.io/result"
    
    payload = json.dumps({
        "resultId": data
        })
    headers = {
        'Authorization': '4acfb935-d254-4e29-8ff6-719de465dce1',
        'Content-Type': 'application/json'
        }
    while True:
        
        response = requests.request("POST", url, headers=headers, data=payload)

        data: dict=response.json()
        if "percentage" in data.keys():
            message_id = callback.message.message_id
            chat_id = callback.message.chat.id
            new_text = f'process: {data["percentage"]}%'

            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_text)

        elif "imageURL" in data.keys():
            break
        
    img_url=data["imageURL"]
    db.add_image(a,b,img_url)
    return img_url


def get_json(description: str,a,b,callback,bot):
    url = "https://api.midjourneyapi.io/imagine"
    mid_token='4acfb935-d254-4e29-8ff6-719de465dce1'
    payload = json.dumps({
    "prompt": description,
    "callbackURL": "azamovanas.pythonanywhere.com/mid"
    })
    headers = {
    'Authorization': mid_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data=response.json()["resultId"]
    
    return download_image(get_result(data,a,b,callback,bot),"image.jpg")

