import telebot
import sqlite3
import time
import datetime
import os
from dotenv import load_dotenv

# База данных
connection = sqlite3.connect('reminders.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS reminders (id INTEGER PRIMARY KEY, user_id INTEGER, reminder TEXT, time TEXT)')
connection.commit()
connection.close()

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

print("Бот запущен")
# Стартовое сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}👽\nЯ бот для напоминаний.")
    print(message.from_user.id, message.from_user.username)
    time.sleep(1)
    bot.send_message(message.from_user.id, "Отправь мне:\n/remind - создать напоминие\n/show - посмотреть все напоминания")
    
bot.polling(none_stop=True)