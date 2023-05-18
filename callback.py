from telegram import Update
from telegram.ext import CallbackContext
from core import DB,generate_image,to_translate

db=DB()

def start(update: Update, callback: CallbackContext):
   
    chat_id=update.message.chat.id
    first_name=update.message.chat.full_name
    user_name=update.message.chat.username
    
    result=db.add_user(chat_id=chat_id,first_name=first_name,username=user_name)
    if result:
        btn=ReplyKeyboardMarkup([["🇺🇿 O'zbk tili"],["🇷🇺 русский язык"]],resize_keyboard=True)
        update.message.reply_html('''Выберите разговорный язык для вашего удобства

                                     Qulaylik uchun so'zlashuv tilini tanlang

                                     Choose a conversational language for your convenience''',reply_markup=btn)

    else:
        btn=ReplyKeyboardMarkup([["🇺🇿 O'zbek tili"],["🇷🇺 русский язык"]],resize_keyboard=True)
        update.message.reply_html('''Выберите разговорный язык для вашего удобства

Qulaylik uchun so'zlashuv tilini tanlang

Choose a conversational language for your convenience''',reply_markup=btn)
        