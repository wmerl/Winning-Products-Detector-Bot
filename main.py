import threading

from pyrogram import idle
from pyrogram import filters, Client

from vars import Vars
from flask import Flask

app = Client(
    "potato_motato",
    api_id=Vars.API_ID, api_hash=Vars.API_HASH
)


@app.on_message(filters.command(['start']) & filters.private)
async def start(c: Client, m):
    chat_id = m.chat.id
    await c.send_message(
        chat_id=chat_id,
        text="I'm Live"
    )


@app.on_message(filters.channel & filters.text)
async def forward_message_text(c, m):
    chat_id = m.chat.id
    entities = m.entities
    msg_text = m.text

    if chat_id == Vars.FROM_CHANNEL_ID:

        await c.send_message(
            chat_id=Vars.TO_GROUP_ID,
            text=msg_text,
            entities=entities,
            reply_to_message_id=16
        )


@app.on_message(filters.channel & filters.photo)
async def forward_message_photo(c, m):
    print(m)

    chat_id = m.chat.id
    caption_entities = m.caption_entities
    caption = m.caption
    photo = m.photo.file_id

    if chat_id == Vars.FROM_CHANNEL_ID:
        await c.send_photo(
            chat_id=Vars.TO_GROUP_ID,
            photo=photo,
            caption=caption,
            caption_entities=caption_entities,
            reply_to_message_id=16
        )


@app.on_message(filters.channel & filters.video)
async def forward_message_video(c, m):

    chat_id = m.chat.id
    caption_entities = m.caption_entities
    caption = m.caption
    video = m.video.file_id

    if chat_id == Vars.FROM_CHANNEL_ID:
        await c.send_video(
            chat_id=Vars.TO_GROUP_ID,
            video=video,
            caption=caption,
            caption_entities=caption_entities,
            reply_to_message_id=16
        )


web_app = Flask(__name__)


@web_app.route('/')
def web_app_live():
    return "Web App is Live!"


if __name__ == '__main__':

    app.start()
    threading.Thread(target=web_app.run, args=("0.0.0.0", 8080), daemon=True).start()

    print("I'm live")

    idle()
    app.stop()

