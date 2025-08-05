import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger(log_level=logging.INFO):
    logger = logging.getLogger("bot_logger")
    logger.setLevel(log_level)

    # جلوگیری از اضافه شدن چند هندلر
    if not logger.handlers:
        # فرمت نمایش لاگ
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S")

        # هندلر برای نمایش در کنسول
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # هندلر برای ذخیره در فایل (با حجم محدود و چرخشی)
        file_handler = RotatingFileHandler("app/logs/bot.log", maxBytes=5_000_000, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
