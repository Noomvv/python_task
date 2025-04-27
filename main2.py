import telebot
import time
import threading
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
print('Бот запущен')

reminders = {}

def reminder_thread(chat_id, message, delay):
    time.sleep(delay)
    bot.send_message(chat_id, message)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}👽\n/remind")

@bot.message_handler(commands=['remind'])
def set_reminder(message):
    bot.reply_to(message, "Напиши время в секундах и сообщение")

    delay = int()
    chat_id = message.chat.id
    
    threading.Thread(target=reminder_thread, args=(chat_id, message, delay)).start()
    bot.reply_to(message, "Напоминание установлено")

bot.polling(none_stop=True)
