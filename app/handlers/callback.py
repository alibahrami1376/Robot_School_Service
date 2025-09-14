
from telebot import TeleBot
from telebot.types import CallbackQuery


def callback_handelers(bot:TeleBot):
        
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call:CallbackQuery):

        match call.data :
           
            case "Driver":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id,"Driver")
            case "Student":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id,"Student")
            case "Contact_us":
                bot.delete_message(call.message.chat.id, call.message.message_id)    
                bot.send_message(call.message.chat.id,"Contact_us")
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
        