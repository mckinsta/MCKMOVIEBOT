from pyrogram import Client, filters
from database import movies
from config import LOG_CHANNEL

@Client.on_message(filters.chat(LOG_CHANNEL))
async def auto_save(client, message):
    if message.video or message.document:
        file_id = message.video.file_id if message.video else message.document.file_id
        name = message.caption or "movie"

        await movies.insert_one({
            "name": name.lower(),
            "file_id": file_id
        })
