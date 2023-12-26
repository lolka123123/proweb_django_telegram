from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def generate_alphabet():
    markup = InlineKeyboardMarkup()

    lst = ['a', 'b', 'c', 'd', 'i', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

    all_words = InlineKeyboardButton(text='Все слова', callback_data='alphabet_all')

    buttons = []
    for i in lst:
        buttons.append(InlineKeyboardButton(text=i, callback_data=f'alphabet_{i}'))

    cansel = InlineKeyboardButton(text='Отмена', callback_data='alphabet_cansel')

    markup.row(all_words)
    markup.add(*buttons)
    markup.row(cansel)

    return markup

def generate_delete_message():
    markup = InlineKeyboardMarkup()

    delete = InlineKeyboardButton(text='Закрыть', callback_data='delete_message')

    markup.row(delete)

    return markup

