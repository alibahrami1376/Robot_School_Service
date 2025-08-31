
from telebot import TeleBot
from telebot.types import Message
from app.core.logger import LogService

def middleware_handeler(bot:TeleBot):
    # تعریف یک میدلور قبل از همه‌ی هندلرها
    @bot.middleware_handler(update_types=['message'])
    def before_handler(bot_instance, message: Message):
        LogService._root.debug(f" message Received :, {message.text} {message.chat.id}")
        # اینجا می‌تونی لاگ، اعتبارسنجی یا هر منطق دیگه بذاری

    # میدلور بعد از هندلرها
    @bot.middleware_handler(update_types=['message'])
    def after_handler(bot_instance, message: Message):
        LogService._root.debug(f"هندلرها پردازش شدن: :, {message.text} {message.chat.id}")
        

