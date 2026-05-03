from pyrogram import Client, filters

@Client.on_message(filters.command("test"))
async def test(client, message):
    await message.reply("Bot working ✅")
