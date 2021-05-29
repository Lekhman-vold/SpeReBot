from flask import Flask, request
from config import API_KEY, NGROK
import telebot


bot = telebot.TeleBot(API_KEY)
bot.set_webhook(url=NGROK)
app = Flask(__name__)


@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "ok"


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hello!')


if __name__ == "__main__":
    app.run()
