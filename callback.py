from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove
from telegram.ext import CallbackContext
from core import DB,get_json,to_translate

db=DB()

def start(update: Update, callback: CallbackContext):
   
    chat_id=update.message.chat.id
    result=db.get_contains(chat_id=chat_id)
    
    if result:
        
        code=db.get_code(chat_id)
        if code=="uz":
            text="Qayta xush kelibsiz"
        elif code=="ru":
            text="Добро пожаловать назад"
        elif code=="en":
            text="Welcome back"
        
        
        
        update.message.reply_html(text)

    else:
        btn=ReplyKeyboardMarkup([["🇺🇿 O'zbek tili"],["🇷🇺 Русский язык"],["🇺🇸 English language"]],resize_keyboard=True)
        update.message.reply_html('''Выберите разговорный язык для вашего удобства

Qulaylik uchun so'zlashuv tilini tanlang

Choose a conversational language for your convenience''',reply_markup=btn)
        
def uz(update: Update, callback: CallbackContext):
        
    db.add_user(update.message.chat_id,update.message.chat.username,update.message.chat.full_name,"uz")      
    
    update.message.reply_html("Chizdirmoqchi bo'lgan rasmingizni tariflab yuboring",reply_markup=ReplyKeyboardRemove())  
    
def ru(update: Update, callback: CallbackContext):
        
    db.add_user(update.message.chat_id,update.message.chat.username,update.message.chat.full_name,"ru")      
    
    update.message.reply_html("Пожалуйста, опишите картину, которую вы хотите сделать",reply_markup=ReplyKeyboardRemove())  
    
def en(update: Update, callback: CallbackContext):
        
    db.add_user(update.message.chat_id,update.message.chat.username,update.message.chat.full_name,"en")      
    
    update.message.reply_html("Please describe the image you want to create",reply_markup=ReplyKeyboardRemove())  
    
    
def image(update: Update, callback: CallbackContext):
    chat_id=update.message.chat_id
    code=db.get_code(chat_id)
    if code=="uz":
        text="Jarayon bir necha soniya vaqt olishi mumkin"
    elif code=="ru":
        text="Процесс может занять несколько секунд"
    elif code=="en":
        text="The process may take a few seconds"
        
    db.add_task(update.message.chat_id,update.message.chat.full_name,update.message.text)
        
    update.message.reply_html(text)
    data=get_json(to_translate(update.message.text),update.message.chat_id,update.message.chat.full_name,update,callback)
    update.message.reply_photo(data)
    update.message.reply_document(data)
    
    
    