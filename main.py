from webhook import *
from models import User


@bot.message_handler(commands=['start'])
def start_command(message):
    print("Start fun")
    bot.send_message(message.chat.id, 'Welcome to Notatnik Bot!')


@bot.message_handler(commands=['get'])
def add_db(message):
    print("get func")
    # db.session.add(User(username="George", email="exaple@exaple.com"))
    # db.session.commit()
    users = User.query.all()

    bot.send_message(message.chat.id, users)


if __name__ == "__main__":
    app.run()
