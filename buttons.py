from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def remind_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton('Напомнить'))
    return kb