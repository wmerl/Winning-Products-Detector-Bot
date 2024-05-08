from pyrogram import filters
from bot import app
from vars import Vars


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

