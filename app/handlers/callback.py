
from telebot import TeleBot
from telebot.types import CallbackQuery
from app.views.keyboards import driver_mark,student_mark
from app.Text_messages.system import SystemMessages
from app.core.session import session

def callback_handelers(bot:TeleBot):
        
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call:CallbackQuery):

        match call.data :
           
            case "Driver":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                message= bot.send_message(call.message.chat.id,SystemMessages.CHOICE,reply_markup=driver_mark)
                session.set_last_messageid(call.from_user.id,message.message_id)

            case "Student":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                message = bot.send_message(call.message.chat.id,SystemMessages.CHOICE,reply_markup=student_mark)
                session.set_last_messageid(call.from_user.id,message.message_id)

            case "Contact_us":
                bot.delete_message(call.message.chat.id, call.message.message_id)    
                message= bot.send_message(call.message.chat.id,"Contact_us")
                session.set_last_messageid(call.from_user.id,message.message_id)

            case "reg_ST":
                pass
            case "info_ST":
                pass
            case "Financial_ST":
                pass
            case "reg_DR":
                pass
            case "info_DR":
                pass
            case "Financial_DR":
                pass    
        