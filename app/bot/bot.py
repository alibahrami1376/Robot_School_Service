
from app.bot.connection_manager import create_bot_with_retry,run_bot_white_try


def run():
    bot = create_bot_with_retry()
    run_bot_white_try(bot)
   

