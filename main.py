from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# 🔥 Bot client (plugins load होणार)
app = Client(
    "movie_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")
)

# 🔥 Dummy server (Koyeb साठी)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

print("🚀 Bot Starting...")

# 🔥 Debug (IMPORTANT)
print("TOKEN:", BOT_TOKEN)

# 🔥 Quick test (guarantee working)
@app.on_message(filters.command("hi"))
async def hi(client, message):
    await message.reply("Hello working ✅")

# 🔥 Run bot
app.run()
