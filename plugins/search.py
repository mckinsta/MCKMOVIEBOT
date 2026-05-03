from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import movies

@Client.on_message(filters.text & filters.private)
async def search(client, message):
    query = message.text.lower()

    results = movies.find({"name": {"$regex": query}})

    buttons = []
    async for m in results:
        buttons.append([InlineKeyboardButton(m["name"], callback_data=m["file_id"])])

    if not buttons:
        return await message.reply("❌ Movie not found")

    await message.reply(
        "🔍 Results:",
        reply_markup=InlineKeyboardMarkup(buttons[:10])
    )


@Client.on_callback_query()
async def send_movie(client, query):
    file_id = query.data
    await client.send_video(query.message.chat.id, file_id)
