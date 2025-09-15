from telebot import TeleBot
from telebot.types import Message
from app.views.keyboards import main_mark
from app.Text_messages.system import SystemMessages
from app.core.logger import LogService

from app.core.session import session




def Start(bot:TeleBot):
    LogService._root.debug("handelers.start.register.start")

    @bot.message_handler(commands=['start'])
    def handle_start(m: Message):
        if session.sessions.get(m.from_user.id) is None:
            session.start(m)  
        else :
            bot.delete_message(m.chat.id,session.get_last_messageid(m.from_user.id))    
        message = bot.send_message(m.chat.id,SystemMessages.WELCOME_START,reply_markup=main_mark)
        session.set_last_messageid(m.from_user.id,message.message_id)


