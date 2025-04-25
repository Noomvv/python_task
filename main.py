import telebot
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

print("Бот запущен")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, f"Приветствую тебя {message.from_user.first_name}!")
    
bot.polling(none_stop=True)