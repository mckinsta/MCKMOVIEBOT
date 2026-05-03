from pyrogram import Client, filters
from config import QR, UPI_ID

@Client.on_message(filters.command("donate"))
async def donate(client, message):
    await message.reply_photo(
        photo=QR,
        caption=f"💰 Support Us\n\nUPI: {UPI_ID}"
    )
