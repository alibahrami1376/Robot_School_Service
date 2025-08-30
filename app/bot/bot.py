
from app.bot.connection_manager import create_bot_with_retry,run_bot_white_try
from app.handlers.start import register

def run():
    bot = create_bot_with_retry()
    register(bot)
    run_bot_white_try(bot)
   

