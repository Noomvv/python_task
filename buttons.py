from telebot import types


def remind_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    remind_btn = types.KeyboardButton('Напомнить')
    kb.add(remind_btn)
    return kb