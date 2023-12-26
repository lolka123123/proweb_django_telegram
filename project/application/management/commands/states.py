from telebot.handler_backends import State, StatesGroup

class States(StatesGroup):
    start = State()
    translate = State()
    translate_to = State()
    translate_word = State()
    alphabet = State()