from flask import Flask, request
from secure.config import API_KEY, NGROK, POSTGRES_USER, POSTGRES_PASSWORD
import telebot

# ------------------ Telegram
bot = telebot.TeleBot(API_KEY)
bot.set_webhook(url=NGROK)

# ------------------- Flask
app = Flask(__name__)

# ------------------- Postgres
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/flaskbot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
