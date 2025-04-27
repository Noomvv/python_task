import telebot
import sqlite3
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
print("Бот запущен")

# Создание базы данных
connection = sqlite3.connect('remind.db', check_same_thread=False)
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS reminders (id INTEGER PRIMARY KEY, user_id INTEGER, reminder TEXT, time TEXT, status TEXT)')
connection.commit()
# connection.close()
print("База данных создана")

# Стартовое сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}👽")
    print(f'Кто это у нас тут: {message.from_user.id, message.from_user.username}')
    time.sleep(1)
    bot.send_message(message.from_user.id, "Отправь мне:\n/remind - создать напоминие\n/show - посмотреть все напоминания")
    
# Создание напоминания
@bot.message_handler(commands=['remind'])

def remind_message(message):
    bot.send_message(message.from_user.id, "Напиши текст напоминания")
    bot.register_next_step_handler(message, get_remind_text)

def get_remind_text(message):
    reminder_text = message.text
    bot.send_message(message.from_user.id, "Напиши время в формате ЧЧ:ММ")
    bot.register_next_step_handler(message, get_remind_time, reminder_text_from_prev_step=reminder_text)

def get_remind_time(message, reminder_text_from_prev_step):
    sql.execute('INSERT INTO reminders (user_id, reminder, time, status) VALUES (?, ?, ?, ?)', (message.from_user.id, reminder_text_from_prev_step, message.text, 'active'))
    connection.commit()
    # connection.close()
    bot.send_message(message.from_user.id, "Напоминание создано")
    print('Все в порядке, продолжаем:)')

bot.polling(none_stop=True)