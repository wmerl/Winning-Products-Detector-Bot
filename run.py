import threading

from pyrogram import idle
from bot import app
from flask import Flask


web_app = Flask(__name__)


@web_app.route('/')
def index():
    return "Bot is Live!"
    


threading.Thread(target=web_app.run, args=()).start()

app.start()
print("I'm live")

idle()
app.stop()

