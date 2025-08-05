from app.bot.bot import run
import logging
from app.logger import setup_logger
from app.bot.bot import settings


log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
logger = setup_logger(log_level=log_level)

logger.info(f"سطح لاگ: {settings.LOG_LEVEL}")

if __name__ == "__main__":
    run()
