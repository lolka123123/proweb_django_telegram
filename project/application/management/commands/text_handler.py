from telebot.types import Message, ReplyKeyboardRemove
from .loader import bot
from .keyboadrs.reply import generate_start, generate_translate, generate_translate_to
from .keyboadrs.inline import generate_alphabet
from .states import States
from translate import Translator
from .data import LANGUAGES

from application import models


@bot.message_handler(commands=['start'])
def start(message: Message):
    profile = models.Profile.objects.filter(telegram_id=message.from_user.id)
    if not profile.exists():
        models.Profile.objects.create(telegram_id=message.from_user.id, full_name=message.from_user.full_name,
                                      user_name=message.from_user.username)
    text = f'<b>Привет {message.from_user.full_name}!\nВыбор функцию:</b>'
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=generate_start())

    bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
    bot.set_state(user_id=message.from_user.id, state=States.start, chat_id=message.chat.id)

@bot.message_handler(state=States.start)
def functions(message: Message):
    if message.text == 'Переводчик':
        text = '<b>Выберите язык:</b>'
        bot.send_message(text=text, chat_id=message.chat.id, reply_markup=generate_translate())

        bot.set_state(user_id=message.from_user.id, state=States.translate, chat_id=message.chat.id)

    elif message.text == 'Словарь':
        msg = bot.send_message(chat_id=message.chat.id, text='.', reply_markup=ReplyKeyboardRemove())
        bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
        text = '<b>Выберите букву:</b>'
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=generate_alphabet())

        bot.set_state(user_id=message.from_user.id, state=States.alphabet, chat_id=message.chat.id)



@bot.message_handler(state=States.translate)
def translate(message: Message):
    text = '<b>Выберите язык перевода:</b>'
    if message.text == 'Назад':
        bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
        bot.set_state(user_id=message.from_user.id, state=States.start, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'<b>Привет {message.from_user.full_name}!\nВыбор функцию:</b>',
                         reply_markup=generate_start())
    else:
        for key, value in LANGUAGES.items():
            if message.text == value:
                msg = bot.send_message(text='.', chat_id=message.chat.id, reply_markup=ReplyKeyboardRemove())
                bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)

                bot.set_state(user_id=message.from_user.id, state=States.translate_to, chat_id=message.chat.id)
                with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                    data['lang'] = key
                bot.send_message(text=text, chat_id=message.chat.id, reply_markup=generate_translate_to(key))

@bot.message_handler(state=States.translate_to)
def translate_to(message: Message):
    text = '<b>Чтоб вернуться назад, нажмите /stop\nВведите слово для перевода:</b>'
    if message.text == 'Назад':
        text = '<b>Выберите язык:</b>'
        bot.send_message(text=text, chat_id=message.chat.id, reply_markup=generate_translate())

        bot.set_state(user_id=message.from_user.id, state=States.translate, chat_id=message.chat.id)
    else:
        for key, value in LANGUAGES.items():
            if message.text == value:
                bot.send_message(text=text, chat_id=message.chat.id, reply_markup=ReplyKeyboardRemove())

                bot.set_state(user_id=message.from_user.id, state=States.translate_word, chat_id=message.chat.id)
                with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                    data['lang_to'] = key


@bot.message_handler(state=States.translate_word)
def translate_word(message: Message):
    if message.text == '/stop':
        bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
        bot.set_state(user_id=message.from_user.id, state=States.start, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'<b>Привет {message.from_user.full_name}!\nВыбор функцию:</b>',
                         reply_markup=generate_start())
    else:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            lang = data['lang']
            lang_to = data['lang_to']

            try:
                translator = Translator(from_lang=lang, to_lang=lang_to)
                translation = translator.translate(message.text)

                profile = models.Profile.objects.get(telegram_id=message.from_user.id)
                models.Word.objects.create(profile=profile, word=message.text,
                                           translated_word=translation, translated_language=lang,
                                           translated_to_language=lang_to)

                bot.send_message(chat_id=message.chat.id, text=translation)
            except:
                bot.send_message(chat_id=message.chat.id, text='<b>Такого слова не существует</b>')
