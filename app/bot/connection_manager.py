import time
from telebot import TeleBot,apihelper
import requests
from app.core.config import get_settings
from app.Text_messages.logs import LogMessages
from app.core.logger import LogService

settings = get_settings()

RETRY_INTERVAL = 10 # ثانیه بین هر تلاش مجدد

def create_bot_with_retry(middleware:bool = False):
    
    LogService._root.debug("Bot.connection_manager.create_bot_with_retry.start")

    while True:
        try:
            LogService._root.debug(LogMessages.STARTUP_TRY_CONNECT)
            if middleware:
                apihelper.ENABLE_MIDDLEWARE = True  
            bot = TeleBot(settings.BOT_TOKEN)
            bot.get_me()  # بررسی اتصال واقعی
            LogService._root.debug(LogMessages.STARTUP_SUCCESS)
            return bot

        except requests.exceptions.RequestException:
            LogService._root.warning(LogMessages.UNEXPECTED_SHUTDOWN)
            time.sleep(RETRY_INTERVAL)

        except Exception as e:
            LogService._root.exception(LogMessages.STARTUP_FAILED.format(error=e))
            time.sleep(RETRY_INTERVAL)


def run_bot_white_try(bot:TeleBot):
    LogService._root.debug("Bot.connection_manager.run_bot_white_try.start")

    while True:
        
        try:
            LogService._root.info("🔥 Bot starting...")
            bot.polling(non_stop=True)
        except requests.exceptions.ProxyError:
            LogService._root.warning("⚠️ Proxy Error. Retrying in %s seconds...", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)
        except requests.exceptions.RequestException:
            LogService._root.warning("❌ Unexpected shutdown. Retrying in %s seconds...", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)
        except requests.exceptions.ConnectionError:
            LogService._root.warning("❌ConnectionError   %s seconds ", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)
        except requests.exceptions.Timeout:
            LogService._root.warning("❌ Timeout   %s seconds ", RETRY_INTERVAL)
            time.sleep(RETRY_INTERVAL)    
        except Exception as e:
            LogService._root.exception("🚨 Unknown error: %s", e)
            time.sleep(RETRY_INTERVAL)