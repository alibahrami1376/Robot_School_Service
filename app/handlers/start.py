from telebot.types import Message
from app.views.keyboards import rep_mark
from app.core.logger import LogService

data = {723644977:"Alibahrami" }

def Start(bot):
    LogService._root.debug("handelers.start.register.start")

    @bot.message_handler(commands=['start'])
    def handle_start(m: Message):

        if m.chat.username is  None:
            bot.send_message(m.chat.id,"please set usrname....")
            return
      
        user = data.get(m.chat.id)

        if user :
            bot.send_message(m.chat.id,F"hi {user} ......")
        else :
            data[m.chat.id]=m.chat.username
            bot.send_message(m.chat.id, "سلام! 👋 به بات خوش اومدی.", reply_markup=rep_mark)




