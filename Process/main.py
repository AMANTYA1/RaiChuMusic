from pyrogram import Client
from RaiChu.config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "RaiChu",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="RaiChu.Player"),
    )

aman = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(aman,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(aman, overload_quiet_mode=True)

with Client("RaiChu", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with aman as app:
    me_aman = app.get_me()
