from pyrogram import Client, filters
from config import LOGO

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_photo(
        photo=LOGO,
        caption="🎬 Welcome to MCK Movie Bot\n\nSend movie name to search 🔍"
    )
