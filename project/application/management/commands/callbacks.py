from telebot.types import  CallbackQuery
from .loader import bot
from .keyboadrs.reply import generate_start
from .keyboadrs.inline import generate_alphabet, generate_delete_message
from .states import States
import json
from .data import LANGUAGES

from application import models


@bot.callback_query_handler(func=lambda call: 'alphabet' in call.data)
def alphabet(call: CallbackQuery):
    data = call.data.split('_')[1]

    text = ''

    if data == 'cansel':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.delete_state(user_id=call.from_user.id, chat_id=call.message.chat.id)
        bot.set_state(user_id=call.from_user.id, state=States.start, chat_id=call.message.chat.id)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f'<b>Привет {call.from_user.full_name}!\nВыбор функцию:</b>',
                         reply_markup=generate_start())

    elif data == 'all':
        profile = models.Profile.objects.get(telegram_id=call.from_user.id)
        words = models.Word.objects.filter(profile=profile)

        for word in words:
            text += f"{word.translated_word} - {word.word} | {LANGUAGES[word.translated_to_language]} - {LANGUAGES[word.translated_language]}\n"

        if text == '':
            bot.edit_message_text(text='<b>Тут пусто</b>', chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=generate_delete_message())
        else:
            bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=generate_delete_message())
    else:
        profile = models.Profile.objects.get(telegram_id=call.from_user.id)
        words = models.Word.objects.filter(profile=profile)

        for word in words:
            if word.translated_word.lower()[0] == data.lower():
                text += f"{word.translated_word} - {word.word} {word.language} | {LANGUAGES[word.translated_to_language]} - {LANGUAGES[word.translated_language]}\n"

        if text == '':
            bot.edit_message_text(text='<b>Тут пусто</b>', chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=generate_delete_message())
        else:
            bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=generate_delete_message())





@bot.callback_query_handler(func=lambda call: 'delete_message' == call.data)
def delete_message(call: CallbackQuery):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.delete_state(user_id=call.from_user.id, chat_id=call.message.chat.id)
    bot.set_state(user_id=call.from_user.id, state=States.start, chat_id=call.message.chat.id)
    bot.send_message(chat_id=call.message.chat.id,
                     text=f'<b>Привет {call.from_user.full_name}!\nВыбор функцию:</b>',
                     reply_markup=generate_start())