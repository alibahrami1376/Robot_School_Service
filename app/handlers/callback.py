
from telebot import TeleBot
from telebot.types import CallbackQuery,Message
from app.views.keyboards import driver_mark,student_mark,back_menu_mark,main_mark
from app.Text_messages.system import SystemMessages
from app.Text_messages.dr_register import DriverRigesterMessage
from app.core.session import session,step





def callback_handelers(bot: TeleBot):

    
    def handle_driver(user_id, chat_id, message_id):
        bot.delete_message(chat_id, message_id)
        message = bot.send_message(chat_id, SystemMessages.CHOICE, reply_markup=driver_mark)
        session.set_last_messageid(user_id, message.message_id)
        session.set_step(user_id, step.DRIVER.value)

    def handle_student(user_id, chat_id, message_id):
        bot.delete_message(chat_id, message_id)
        message = bot.send_message(chat_id, SystemMessages.CHOICE, reply_markup=student_mark)
        session.set_last_messageid(user_id, message.message_id)
        session.set_step(user_id, step.STUDENT.value)

    def handle_contact(user_id, chat_id, message_id):
        bot.delete_message(chat_id, message_id)
        message = bot.send_message(chat_id, "Contact_us")
        session.set_last_messageid(user_id, message.message_id)
        session.set_step(user_id, step.CONTACT_US.value)

    def handle_reg_driver(user_id, chat_id, message_id):

        driver_ask_firstname(user_id, chat_id, message_id)       


    def handle_previous_stage(user_id, chat_id, msg_id,call:CallbackQuery):

        match session.get_step(user_id) : 

            case :
                pass
        
        
        session.get_step_reg(user_id)



        


    def driver_ask_firstname(user_id, chat_id, message_id):

        bot.delete_message(chat_id, message_id)
        message = bot.send_message(chat_id, DriverRigesterMessage.INPUT_FIRST_NAME, reply_markup=back_menu_mark)
        session.set_last_messageid(user_id, message.message_id)
        session.set_step_reg(user_id, 1)

        bot.register_next_step_handler(message, driver_ask_lastname)  

    def driver_ask_lastname(message:Message):
        # name = message.text
        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_LAST_NAME,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 2)
        bot.register_next_step_handler(msg,driver_father_name)


    def driver_father_name(message:Message):

        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_FATHER_NAME,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 3)
        bot.register_next_step_handler(msg,driver_National_code)

    def driver_National_code(message):
        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_NATIONAL_CODE,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 4)
        bot.register_next_step_handler(msg,driver_Insurance_number)

    def driver_Insurance_number(message):

        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_ِDRIVER_INSURANCE_NUMBER,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 5)
        bot.register_next_step_handler(msg,driver_Insurance_images)

    def driver_Insurance_images(message):
        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_ِDRIVER_INSURANCE_IMAGES,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 6)
        bot.register_next_step_handler(msg,driver_Technical_inspection_images)

    def driver_Technical_inspection_images(message):
        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_ِDRIVER_TECHNICAL_INSPECTION_IMAGES,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 7)
        bot.register_next_step_handler(msg,driver_Green_leaf_images)

    def driver_Green_leaf_images(message):
        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_ِDRIVER_GREEN_LEAF_IMAGES,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 8)
        bot.register_next_step_handler(msg,driver_addres_home) 

    def driver_addres_home(message):
        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_ِDRIVER_ADDRESS_HOME,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 9)
        bot.register_next_step_handler(msg,driver_Location_home)

    def driver_Location_home(message):
        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_ِDRIVER_LOCATION_HOME,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id, 10)
        bot.register_next_step_handler(msg,driver_Postal_code)

    def driver_Postal_code(message):

        msg = bot.send_message(message.chat.id,DriverRigesterMessage.INPUT_ِDRIVER_POSTAL_CODE,reply_markup=back_menu_mark)
        session.set_step_reg(message.from_user.id,11)
        bot.register_next_step_handler(msg,driver_reg_final)

    def driver_reg_final(message):
        bot.send_message(message.chat.id,DriverRigesterMessage.FINAL)
        session.set_step_reg(message.from_user.id, 12)
        bot.send_message(message.chat.id,SystemMessages.WELCOME_START,reply_markup=main_mark)


    def handle_main_menu(user_id, chat_id, message_id):
        bot.delete_message(chat_id, message_id)
        message = bot.send_message(chat_id, SystemMessages.WELCOME_START, reply_markup=main_mark)
        session.set_last_messageid(user_id, message.message_id)
        session.set_step(user_id, step.START.value)

    
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call: CallbackQuery):
        user_id = call.from_user.id
        chat_id = call.message.chat.id
        msg_id = call.message.message_id

        match call.data:
            case "Driver":
                handle_driver(user_id, chat_id, msg_id)

            case "Student":
                handle_student(user_id, chat_id, msg_id)

            case "Contact_us":
                handle_contact(user_id, chat_id, msg_id)

            case "reg_DR":
                handle_reg_driver(user_id, chat_id, msg_id)

            case "main_menu":
                handle_main_menu(user_id, chat_id, msg_id)

            case "previous_stage":
                handle_previous_stage(user_id, chat_id, msg_id,call)
            case _:  
                pass

   
    return {
        "driver": handle_driver,
        "student": handle_student,
        "contact": handle_contact,
        "reg_driver": handle_reg_driver,
        "main_menu": handle_main_menu
    }









