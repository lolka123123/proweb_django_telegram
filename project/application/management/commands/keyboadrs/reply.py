from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from ..data import LANGUAGES


def generate_start():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    translate_button = KeyboardButton(text='Переводчик')
    dict_button = KeyboardButton(text='Словарь')

    markup.row(translate_button, dict_button)

    return markup

def generate_translate():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)


    buttons = []
    for key, value in LANGUAGES.items():
        buttons.append(KeyboardButton(text=value))

    cansel = KeyboardButton(text='Назад')

    markup.add(*buttons)
    markup.row(cansel)

    return markup


def generate_translate_to(lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = []
    for key, value in LANGUAGES.items():
        if key == lang:
            continue
        buttons.append(KeyboardButton(text=value))

    cansel = KeyboardButton(text='Назад')

    markup.add(*buttons)
    markup.row(cansel)

    return markup