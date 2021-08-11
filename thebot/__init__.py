import logging
import time
from telegraph import Telegraph
from sample config import Config
from pyrogram import Client, errors
StartTime = time.time()
logging.basicConfig(level=logging.INFO)

telegraph = Telegraph()
telegraph.create_account(short_name='dank')

API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
DB_URI = Config.DB_URI
ALLOWED_USERS = [
        895373440
    ]
LOG_CHANNEL = Config.LOG_CHANNEL

dankbot = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
