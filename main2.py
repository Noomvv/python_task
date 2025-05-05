import os
import threading
from dotenv import load_dotenv
import telebot, buttons
from buttons import remind_button

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}! 👽", reply_markup=buttons.remind_button())

@bot.message_handler(content_types=['text'])
def ask_reminder(message):
    bot.send_message(message.from_user.id, "Введите через сколько секунд и текст напоминания (пример: 10 Купить хлеб)")

@bot.message_handler(content_types=['text'])
def set_reminder(message):
    parts = message.text.split(' ', 1)
    delay = int(parts[0])
    reminder_text = parts[1].strip()
    threading.Timer(delay, lambda: bot.send_message(message.chat.id, reminder_text)).start()
    bot.send_message(message.chat.id, "Напоминание установлено!")

if __name__ == '__main__':
    print('Бот запущен')
    bot.infinity_polling()