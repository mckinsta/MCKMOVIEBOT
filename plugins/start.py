from pyrogram import Client, filters
from config import LOGO, OWNER

@Client.on_message(filters.command("start"))
async def start(client, message):
    text = f"""
🎬 Welcome to Movie Bot

👤 Owner: {OWNER}

🔍 Send movie name to search
💰 Use /donate to support
"""

    if LOGO:
        await message.reply_photo(
            photo=LOGO,
            caption=text
        )
    else:
        await message.reply(text)
