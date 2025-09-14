
from app.bot.connection_manager import create_bot_with_retry,run_bot_white_try
from app.handlers.start import Start
from app.core.logger import LogService
from app.handlers.middleware import middleware_handeler
from app.handlers.callback import callback_handelers
def run():
    LogService._root.debug("Bot.bot.run.start")
    bot = create_bot_with_retry(middleware=True)
    middleware_handeler(bot)
    callback_handelers(bot)
    Start(bot)
    run_bot_white_try(bot)
   

