
from app.bot.connection_manager import create_bot_with_retry,run_bot_white_try
from app.handlers.start import register
from app.core.logger import LogService
from app.handlers.middleware import middleware_handeler
def run():
    LogService._root.debug("Bot.bot.run.start")
    bot = create_bot_with_retry(middleware=True)
    middleware_handeler(bot)
    register(bot)
    run_bot_white_try(bot)
   

