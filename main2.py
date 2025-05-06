import os
import threading
from dotenv import load_dotenv
import telebot, buttons
from buttons import remind_button

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
DEV_ID = os.getenv('DEV_ID')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}! 👽", reply_markup=buttons.remind_button())


@bot.message_handler(content_types=['text'])
def ask_text(message):
    remind_text = bot.send_message(message.from_user.id, "Что тебе напомнить?🫦")
    bot.register_next_step_handler(remind_text, ask_delay)

def ask_delay(message):
    reminder_text = message.text
    delay_text = bot.send_message(message.from_user.id, "Через сколько секунд напомнить?🥸")
    bot.register_next_step_handler(delay_text, set_reminder, reminder_text)

def set_reminder(message, reminder_text):
    delay = int(message.text)
    t = threading.Timer(delay, lambda: bot.send_message(message.from_user.id, f'{message.from_user.first_name}, не забудь {reminder_text}'))
    t.start()
    bot.send_message(message.from_user.id, "Готово!🙂‍↕️")
    bot.send_message(DEV_ID, f'Вашим ботом воспользовался юзер {message.from_user.first_name}')
    
print("Я готов!!!")
bot.polling(none_stop=True)