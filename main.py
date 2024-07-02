import threading

from pyrogram import idle
from pyrogram import filters, Client
from pyrogram.enums import ParseMode

from vars import Vars
from flask import Flask
from datetime import datetime


# region Helpers
async def send_photo(c: Client, photo, date_hour) -> None:

    # Send photo to the Topic
    await c.send_photo(
        chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
        photo=photo,
        caption=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )

    # Sending photo to Winner & Viral Products Channel
    await c.send_photo(
        chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
        photo=photo,
        caption=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )


async def send_video(c: Client, video, date_hour) -> None:
    # Send video to the Topic
    await c.send_video(
        chat_id=Vars.DROPSHIPPING_COMMUNITY_GROUP_ID,
        video=video,
        caption=Vars.TOPIC_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )

    # Sending video to Winner & Viral Products Channel
    await c.send_video(
        chat_id=Vars.WINNER_AND_VIRAL_PRODUCTS_CHANNEL_ID,
        video=video,
        caption=Vars.PUBIC_CHANNEL_CAPTION.format(date_hour=date_hour),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=Vars.SEGNALI_PODOTTI_TOPIC_ID
    )
# endregion


app: Client = Client(
    "TendencyWins",
    api_id=Vars.API_ID, api_hash=Vars.API_HASH
)


# region Start command handler
@app.on_message(filters.command(['start']) & filters.private)
async def start(c: Client, m):
    chat_id = int(m.chat.id)
    await c.send_message(
        chat_id=chat_id,
        text="I'm Live"
    )
# endregion




# region Photo Handlers (int id)
# WINNING_LAB_CHANNEL_ID Channel photo Handler (int id)
@app.on_message(filters.photo & filters.chat(Vars.WINNING_LAB_CHANNEL_ID))
async def forward_message_winning_lab_photo_int_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    photo = m.photo.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_photo(c, photo, date_hour)


# DAILY_VIRAL_PRODUCTS_CHANNEL_ID Channel Handler (int id)
@app.on_message(filters.photo & filters.chat(Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID))
async def forward_message_daily_viral_products_photo_int_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    photo = m.photo.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_photo(c, photo, date_hour)
# endregion
# region Video Handlers (int id)
# WINNING_LAB_CHANNEL_ID Channel Video Handler (int id)
@app.on_message(filters.video & filters.chat(Vars.WINNING_LAB_CHANNEL_ID))
async def forward_message_winning_lab_video_int_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    video = m.video.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_video(c, video, date_hour)


# DAILY_VIRAL_PRODUCTS_CHANNEL_ID Channel Video Handler (int id)
@app.on_message(filters.video & filters.chat(Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID))
async def forward_message_daily_viral_products_video_int_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    video = m.video.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_video(c, video, date_hour)
# endregion




# region Photo Handlers (str id)
# WINNING_LAB_CHANNEL_ID Channel photo Handler
@app.on_message(filters.photo & filters.chat('winninglab'))
async def forward_message_winning_lab_photo_str_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    photo = m.photo.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_photo(c, photo, date_hour)


# DAILY_VIRAL_PRODUCTS_CHANNEL_ID Channel Photo Handler
@app.on_message(filters.photo & filters.chat('venditeonlieita'))
async def forward_message_daily_viral_products_photo_str_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    photo = m.photo.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_photo(c, photo, date_hour)
# endregion
# region Video Handlers (str id)
# WINNING_LAB_CHANNEL_ID Channel Video Handler
@app.on_message(filters.video & filters.chat('winninglab'))
async def forward_message_winning_lab_video_str_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    video = m.video.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_video(c, video, date_hour)


# DAILY_VIRAL_PRODUCTS_CHANNEL_ID Channel Video Handler (int id)
@app.on_message(filters.video & filters.chat('venditeonlieita'))
async def forward_message_daily_viral_products_video_str_id(c: Client, m):
    chat_id = int(m.chat.id)
    # entities = m.entities
    # msg_text = m.text
    video = m.video.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    await send_video(c, video, date_hour)
# endregion





# region Photo handler
@app.on_message(filters.photo)
async def forward_message_photo(c: Client, m):

    chat_id = int(m.chat.id)
    # caption_entities = m.caption_entities
    # caption = m.caption
    photo = m.photo.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    if chat_id in [Vars.WINNING_LAB_CHANNEL_ID, Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID]:

        await send_photo(c, photo, date_hour)
# endregion
# region Video handler
@app.on_message(filters.video)
async def forward_message_video(c: Client, m):

    chat_id = int(m.chat.id)
    # caption_entities = m.caption_entities
    # caption = m.caption
    video = m.video.file_id

    now = datetime.now()
    date_hour = now.strftime("%Y-%m-%d %H:%M")

    if chat_id in [Vars.WINNING_LAB_CHANNEL_ID, Vars.DAILY_VIRAL_PRODUCTS_CHANNEL_ID]:

        await send_video(c, video, date_hour)

# endregion





# region Text Handler
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
# endregion





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

