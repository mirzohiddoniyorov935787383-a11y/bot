import telebot
import os

# BOT_TOKEN Railway.environmentdan olinadi
BOT_TOKEN = os.getenv("8341758119:AAEi9sEFUUMWWe4OxuGoHekPb_91iy5XYXI")
bot = telebot.TeleBot(8341758119:AAEi9sEFUUMWWe4OxuGoHekPb_91iy5XYXI)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Bot ishga tushdi 😊")

bot.polling()
