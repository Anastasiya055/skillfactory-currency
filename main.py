import telebot
import config
from extensions import Api

token = config.urls.TG_API_KEY

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  print('=>>>>>>', message.text)
  splitted_msg = message.text.split(' ')
  base = splitted_msg[0]
  quote = splitted_msg[1]
  amount = splitted_msg[2]
  result = Api.get_price(base, quote, amount)
  bot.reply_to(message, result)

bot.polling()