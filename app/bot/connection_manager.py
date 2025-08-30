import time
from telebot import TeleBot
import requests
from app.core.config import get_settings
from app.core.logger import setup_logger
from app.Text_messages.logs import LogMessages

logger = setup_logger()

RETRY_INTERVAL = 10 # ثانیه بین هر تلاش مجدد

settings = get_settings()

def create_bot_with_retry():
    

    while True:
        try:
            logger.info(LogMessages.STARTUP_TRY_CONNECT)
            bot = TeleBot(settings.BOT_TOKEN)
            bot.get_me()  # بررسی اتصال واقعی
            logger.info(LogMessages.STARTUP_SUCCESS)
            return bot

        except requests.exceptions.RequestException:
            logger.warning(LogMessages.UNEXPECTED_SHUTDOWN)
            time.sleep(RETRY_INTERVAL)

        except Exception as e:
            logger.exception(LogMessages.STARTUP_FAILED.format(error=e))
            time.sleep(RETRY_INTERVAL)


def run_bot_white_try(bot:TeleBot):
    
    while True:
        try:
            logger.info("🔥 Bot starting...")
            bot.polling(non_stop=True)
        except requests.exceptions.ProxyError:
            logger.warning("⚠️ Proxy Error. Retrying in %s seconds...", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)
        except requests.exceptions.RequestException:
            logger.warning("❌ Unexpected shutdown. Retrying in %s seconds...", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)
        except requests.exceptions.ConnectionError:
            logger.warning("❌ConnectionError   %s seconds ", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)
        except requests.exceptions.Timeout:
            logger.warning("❌ Timeout   %s seconds ", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)    
        except Exception as e:
            logger.exception("🚨 Unknown error: %s", e)
            time.sleep(RETRY_INTERVAL)