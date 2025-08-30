from telebot.types import Message
from app.views.keyboards import rep_mark


def register(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(m: Message):
        bot.send_message(m.chat.id, "سلام! 👋 به بات خوش اومدی.", reply_markup=rep_mark)

    # @bot.message_handler(commands=['help'])
    # def handle_help(m: Message):
    #     bot.send_message(m.chat.id, "دستورها: /start /help /btn")

    # @bot.message_handler(commands=['btn'])
    # def handle_btn(m: Message):
    #     bot.send_message(m.chat.id, "یه دکمه inline:", reply_markup=rep_mark)
