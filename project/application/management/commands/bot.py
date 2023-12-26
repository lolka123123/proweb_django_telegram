from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot

from telebot import custom_filters
from .loader import bot

from . import text_handler, callbacks

class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **kwargs):
        bot.add_custom_filter(custom_filters.StateFilter(bot))
        bot.infinity_polling(skip_pending=True)
