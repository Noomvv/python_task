import os
import threading
from dotenv import load_dotenv
import telebot
from buttons import remind_keyboard

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 👽",
        reply_markup=remind_keyboard()
    )

@bot.message_handler(func=lambda m: m.text == 'Напомнить')
def ask_reminder(message):
    bot.send_message(
        message.chat.id,
        "Введите через сколько секунд и текст напоминания (пример: 10 Купить хлеб)"
    )

@bot.message_handler(func=lambda m: True)
def set_reminder(message):
    parts = message.text.split(' ', 1)
    delay = int(parts[0])
    reminder_text = parts[1].strip()
    threading.Timer(delay, lambda: bot.send_message(message.chat.id, reminder_text)).start()
    bot.send_message(message.chat.id, "Напоминание установлено!")

if __name__ == '__main__':
    print('Бот запущен')
    bot.infinity_polling()