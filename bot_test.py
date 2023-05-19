from callback import (start,uz,ru,en,image)
import os
from telegram.ext import (Updater,
                          MessageHandler,
                          CommandHandler,
                          Filters)

TOKEN="6268124547:AAHse-4GSIkxXJMyPs4X6a4CKV4-JZ0zIrA"

def main():
    update=Updater(TOKEN)
    dispatcher = update.dispatcher
    
    dispatcher.add_handler(CommandHandler(command="start",callback=start))
    dispatcher.add_handler(MessageHandler(Filters.text("🇺🇿 O'zbek tili"),callback=uz))
    dispatcher.add_handler(MessageHandler(Filters.text("🇷🇺 Русский язык"),callback=ru))
    dispatcher.add_handler(MessageHandler(Filters.text("🇺🇸 English language"),callback=en))
    dispatcher.add_handler(MessageHandler(Filters.text,callback=image))

    
    update.start_polling()
    update.idle()
    
if __name__=="__main__":
    main()