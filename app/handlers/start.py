from telebot import TeleBot
from telebot.types import Message
from app.views.keyboards import main_mark
from app.Text_messages.system import SystemMessages
from app.core.logger import LogService

data = {723644977:"Alibahrami" }

def Start(bot:TeleBot):
    LogService._root.debug("handelers.start.register.start")

    @bot.message_handler(commands=['start'])
    def handle_start(m: Message):
        bot.send_message(m.chat.id,SystemMessages.WELCOME_START,reply_markup=main_mark)




