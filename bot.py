from pyrogram import Client
from config import *
from uvloop import install
import os, asyncio

if not os.path.exists('downloads'):
    os.makedirs('downloads')

install()

try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

Bot = Client( 'BypassBot' ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN,
    plugins = {
        "root": "plugins"
    },
    workers = 50
)

Bot.LOGGER = LOGGER

Bot.start()

Bot.me = Bot.get_me()
