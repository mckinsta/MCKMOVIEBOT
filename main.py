from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

app = Client(
    "movie_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# ✅ TEST COMMAND (run च्या आधी ठेव)
@app.on_message(filters.command("test"))
async def test(client, message):
    await message.reply("Bot working ✅")


# 🔥 Dummy server for Koyeb
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    server.serve_forever()

threading.Thread(target=run_server).start()

# ✅ शेवटी run
app.run()
