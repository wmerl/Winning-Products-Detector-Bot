from pyrogram import Client
from vars import Vars

app = Client(
    "potato_motato",
    api_id=Vars.API_ID, api_hash=Vars.API_HASH
)

import bot.callbacks
