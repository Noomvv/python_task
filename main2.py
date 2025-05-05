import telebot
import time
import threading
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
print('Бот запущен')

def reminder_thread(chat_id, reminder_text, delay):
    time.sleep(delay)
    bot.send_message(chat_id, reminder_text)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}👽\n/remind - Установить напоминание")

@bot.message_handler(commands=['remind'])
def set_reminder(message):
    bot.reply_to(message, "Напиши время в секундах и сообщение через пробел")

def process_reminder(message):

    parts = message.text.split(" ", 1)
    delay = int(parts[0])
    if len(parts) < 2 or not parts[1]:
        raise ValueError("Не указан текст напоминания")
    reminder_text = parts[1]
    chat_id = message.chat.id
    threading.Thread(target=reminder_thread, args=(chat_id, reminder_text, delay)).start()
    bot.reply_to(message, "Напоминание установлено")

@bot.message_handler(func=lambda message: True)
def reminder_handler(message):
    process_reminder(message)

bot.polling(none_stop=True)
