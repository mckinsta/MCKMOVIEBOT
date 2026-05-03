from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# 🔥 Debug prints (check env variables)
print("🚀 Bot Starting...")
print("TOKEN:", BOT_TOKEN)
print("API_ID:", API_ID)
print("API_HASH:", API_HASH)

# 🔥 Bot client
app = Client(
    "movie_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")
)

# 🔥 Test command (direct main check)
@app.on_message(filters.command("hi"))
async def hi(client, message):
    await message.reply("Hello working ✅")

# 🔥 Dummy server (Koyeb health check)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# 🔥 Run bot
app.run()
