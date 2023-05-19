from flask import Flask,request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler,MessageHandler,Filters
import os
from callback import (start,uz,ru,en,image)

app=Flask(__name__)
TOKEN=os.environ["TOKEN"]

@app.route("/midjourney",methods=["POST","GET"])
def bot():
    
    if request.method == 'GET':
        
        return 'webhook is working!'

    elif request.method == 'POST':
    
        data=request.get_json()
        bot = Bot(TOKEN)
        
        dispatcher=Dispatcher(bot,None,workers=0)
        update: Update=Update.de_json(data)
        
        dispatcher.add_handler(CommandHandler(["start","boshlash"],start))
        dispatcher.add_handler(MessageHandler(Filters.text("🇺🇿 O'zbek tili"),callback=uz))
        dispatcher.add_handler(MessageHandler(Filters.text("🇷🇺 Русский язык"),callback=ru))
        dispatcher.add_handler(MessageHandler(Filters.text("🇺🇸 English language"),callback=en))
        dispatcher.add_handler(MessageHandler(Filters.text,callback=image))
        
        dispatcher.process_update(update)
        
    
    