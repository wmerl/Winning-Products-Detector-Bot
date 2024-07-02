import threading

from pyrogram import idle
from pyrogram import filters, Client
from pyrogram.enums import ParseMode

from vars import Vars
from flask import Flask
from datetime import datetime

app: Client = Client(
    "TendencyWins",
    api_id=Vars.API_ID, api_hash=Vars.API_HASH
)


# Start command handler
@app.on_message(filters.command(['start']) & filters.private)
async def start(c: Client, m):
    chat_id = int(m.chat.id)
    await c.send_message(
        chat_id=chat_id,
        text="I'm Live"
    )







# WINNING_LAB_CHANNEL_ID Channel Handler (int id)
@app.on_message(filters.chat(Vars.WINNING_LAB_CHANNEL_ID))
async def forward_message_winning_lab_int_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    # Send message to the Topic
    await c.send_message(
        chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
        text=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )

    # Sending message to Winner & Viral Products Channel
    await c.send_message(
        chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
        text=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )


# DAILY_VIRAL_PRODUCTS_CHANNEL_ID Channel Handler (int id)
@app.on_message(filters.chat(Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID))
async def forward_message_daily_viral_products_int_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    # Send message to the Topic
    await c.send_message(
        chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
        text=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )

    # Sending message to Winner & Viral Products Channel
    await c.send_message(
        chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
        text=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )







# Winning Lab Channel Channel Handler
@app.on_message(filters.chat('winninglab'))
async def forward_message_winning_lab(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    # Send message to the Topic
    await c.send_message(
        chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
        text=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )

    # Sending message to Winner & Viral Products Channel
    await c.send_message(
        chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
        text=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )


# Daily Viral Products Channel Handler
@app.on_message(filters.chat('venditeonlieita'))
async def forward_message_venditeonlieita(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    # Send message to the Topic
    await c.send_message(
        chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
        text=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )

    # Sending message to Winner & Viral Products Channel
    await c.send_message(
        chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
        text=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )






# Photo handler
@app.on_message(filters.photo)
async def forward_message_photo(c: Client, m):
    print(m)

    chat_id = int(m.chat.id)
    # caption_entities = m.caption_entities
    # caption = m.caption
    photo = m.photo.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    if chat_id in [Vars.WINNING_LAB_CHANNEL_ID, Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID]:

        # Send message to the Topic
        await c.send_photo(
            chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
            photo=photo,
            caption=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )

        # Sending message to Winner & Viral Products Channel
        await c.send_photo(
            chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
            photo=photo,
            caption=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )


# Video handler
@app.on_message(filters.video)
async def forward_message_video(c: Client, m):

    chat_id = int(m.chat.id)
    # caption_entities = m.caption_entities
    # caption = m.caption
    video = m.video.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    if chat_id in [Vars.WINNING_LAB_CHANNEL_ID, Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID]:

        # Send message to the Topic
        await c.send_video(
            chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
            video=video,
            caption=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )

        # Sending message to Winner & Viral Products Channel
        await c.send_video(
            chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
            video=video,
            caption=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )


# Text Handler
@app.on_message(filters.text)
async def forward_message_text(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    if chat_id in [Vars.WINNING_LAB_CHANNEL_ID, Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID]:

        # Send message to the Topic
        await c.send_message(
            chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
            text=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )

        # Sending message to Winner & Viral Products Channel
        await c.send_message(
            chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
            text=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )






# All handlers
@app.on_message(filters.all)
async def forward_message_all(c: Client, m):

    chat_id = int(m.chat.id)
    # caption_entities = m.caption_entities
    # caption = m.caption
    video = m.video.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    if chat_id in [Vars.WINNING_LAB_CHANNEL_ID, Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID]:

        # Send message to the Topic
        await c.send_video(
            chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
            video=video,
            caption=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )

        # Sending message to Winner & Viral Products Channel
        await c.send_video(
            chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
            video=video,
            caption=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
            parse_mode=ParseMode.HTML,
            reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
        )






web_app = Flask(__name__)


# Defined The Route
@web_app.route('/')
def web_app_live():
    return "Web App is Live!"


if __name__ == '__main__':

    app.start()
    threading.Thread(target=web_app.run, args=("0.0.0.0", 8080), daemon=True).start()

    print("I'm live")

    idle()
    app.stop()

