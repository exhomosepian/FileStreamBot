
from pyrogram import Client
from ..vars import Var

StreamBot = Client(
    session_name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN, "6419447243:AAGjIO1KZ7Y22IR8pxTRpPYKEu4SPZlaG-A"
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
