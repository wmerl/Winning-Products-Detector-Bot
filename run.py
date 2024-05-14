import threading

from pyrogram import idle
from bot import app
from flask import Flask


web_app = Flask(__name__)


@web_app.route('/')
def index():
    return "Web App is Live!"


@web_app.route('/run')
def index():
    threading.Thread(target=web_app.run, args=()).start()

    app.start()
    print("I'm live")
    
    idle()
    app.stop()
    
    return "Bot is Live!"
    




