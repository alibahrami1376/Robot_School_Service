
from telebot import TeleBot
from telebot.types import CallbackQuery
from app.views.keyboards import driver_mark,student_mark,back_menu_mark,main_mark
from app.Text_messages.system import SystemMessages
from app.Text_messages.dr_register import DriverRigesterMessage
from app.core.session import session,step

 

def callback_handelers(bot:TeleBot):
        
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call:CallbackQuery):

        match call.data :
           
            case "Driver":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                message= bot.send_message(call.message.chat.id,SystemMessages.CHOICE,reply_markup=driver_mark)
                session.set_last_messageid(call.from_user.id,message.message_id)
                session.set_step(call.from_user.id,step.DRIVER.value)
            case "Student":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                message = bot.send_message(call.message.chat.id,SystemMessages.CHOICE,reply_markup=student_mark)
                session.set_last_messageid(call.from_user.id,message.message_id)
                session.set_step(call.from_user.id,step.STUDENT.value)

            case "Contact_us":
                bot.delete_message(call.message.chat.id, call.message.message_id)    
                message= bot.send_message(call.message.chat.id,"Contact_us")
                session.set_last_messageid(call.from_user.id,message.message_id)
                session.set_step(call.from_user.id,step.CONTACT_US.value)

            case "reg_ST":
                pass

            case "info_ST":
                pass
            case "Financial_ST":
                pass
            case "reg_DR":
                bot.delete_message(call.message.chat.id, call.message.message_id)    
                message= bot.send_message(call.message.chat.id,DriverRigesterMessage.INPUT_FIRST_NAME,reply_markup=back_menu_mark)
                session.set_last_messageid(call.from_user.id,message.message_id)
                session.set_step(call.from_user.id,step.DRIVER_RG_INPUT_NAME.value)
            case "info_DR":
                pass
            case "Financial_DR":
                pass 
            case "previous_stage":
                pass
            case "main_menu":
                bot.delete_message(call.message.chat.id, call.message.message_id)    
                message= bot.send_message(call.message.chat.id,SystemMessages.WELCOME_START,reply_markup=main_mark)
                session.set_last_messageid(call.from_user.id,message.message_id)
                session.set_step(call.from_user.id,step.START.value)       
        