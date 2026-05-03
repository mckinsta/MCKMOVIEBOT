import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")

DATABASE_URI = os.getenv("DATABASE_URI")

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))

ADMINS = [int(x) for x in os.getenv("ADMINS", "").split() if x]

UPI_ID = os.getenv("UPI_ID")
OWNER = os.getenv("OWNER")

LOGO = os.getenv("LOGO")
QR = os.getenv("QR")
