import telebot
from app.config import get_settings
from app.logger import setup_logger
from logging import DEBUG



logger = setup_logger(log_level=DEBUG)


settings = get_settings()
bot = telebot.TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    
    logger.debug("این یک پیام دیباگ است (فقط وقتی سطح DEBUG باشد نمایش داده می‌شود)")
    bot.send_message(message.chat.id, f"سلام! پایگاه داده: {settings.DB_NAME}")
    logger.error("یک خطا رخ داده!")

def run():
    
    logger.info("ربات شروع به کار کرد...")
    bot.infinity_polling()
    logger.info("ربات   پایان به کار کرد...")
