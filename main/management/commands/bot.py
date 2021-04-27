from django.core.management.base import BaseCommand
from show_room.settings import TOKEN
import telebot
from telebot import types
from main.models import Product

class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(TOKEN)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Открыть список продуктов')
        k2 = types.KeyboardButton('Закрыть')
        keyboard.add(k1, k2)

        products = Product.objects.all()

        def inlinekeyboard():
            inline_keyboard_title = types.InlineKeyboardMarkup()
            for product in products:
                index = product.id
                button = types.InlineKeyboardButton(product.title, callback_data=index)
                inline_keyboard_title.add(button)
            return inline_keyboard_title

        @bot.message_handler(commands=['start'])
        def start_message(message):
            chat_id = message.chat.id
            msg = bot.send_message(chat_id, f'Здравствуйте {message.chat.first_name}',
                                   reply_markup=keyboard)
            bot.register_next_step_handler(msg, get_start)

        def get_start(message):
            chat_id = message.chat.id
            if message.text == 'Открыть список продуктов':
                bot.send_message(chat_id, 'Cписок продуктов:', reply_markup=inlinekeyboard())
            else:
                bot.send_message(chat_id, f'Досвидания {message.chat.first_name}')

        def info(index):
            product = Product.objects.get(id=index)
            return product.info_for_bot()

        @bot.callback_query_handler(func=lambda c: True)
        def get_info(c):
            chat_id = c.message.chat.id

            def keyboard():
                inline_keyboard = types.InlineKeyboardMarkup()
                k1 = types.InlineKeyboardButton('Назад к списку', callback_data='back list')
                k2 = types.InlineKeyboardButton('Выход', callback_data='exit')
                inline_keyboard.add(k1, k2)
                return inline_keyboard

            if c.data == 'back list':
                bot.edit_message_text('Вы обратно вернулись в список:', chat_id, c.message.message_id, reply_markup=inlinekeyboard())
            elif c.data == 'exit':
                bot.edit_message_text('Досвидания', chat_id, c.message.message_id, reply_markup=None)
            else:
                bot.edit_message_text(info(c.data), chat_id, c.message.message_id, reply_markup=keyboard())

        bot.polling()
