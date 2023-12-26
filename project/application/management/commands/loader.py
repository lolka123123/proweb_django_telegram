from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from django.conf import settings

state_storage = StateMemoryStorage()
bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, parse_mode='HTML',
              state_storage=state_storage)

