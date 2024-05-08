import threading

from pyrogram import idle
from bot import app
from web import web_app

if __name__ == '__main__':

    threading.Thread(target=web_app.run, args=()).start()

    app.start()
    print("I'm live")

    idle()
    app.stop()

