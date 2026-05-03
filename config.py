BOT_TOKEN = os.environ.get("8743936811:AAF9VWrkq8zMURZtfdpvBLa-i2GiKk9dHN0")
API_ID = int(os.environ.get("22083216" , 0))
API_HASH = os.environ.get("a4c3ce9493061323cbb5741370aa11f1")

ADMINS = [int(x) for x in os.getenv("1489423238", "").split()]

DATABASE_URI = os.environ.get("mongodb+srv://Koushal:Koushal@koushal.zjd00.mongodb.net/?appName=Koushal"
                             )
LOG_CHANNEL = int(os.getenv("-1003913030328", 0))
FORCE_SUB = None  # optional

UPI_ID = os.getenv("morekoushal@oksbi")
OWNER = os.getenv("@morekoushal1444")

LOGO = os.getenv("https://your-logo-link.jpg")
QR = os.getenv("https://your-qr-link.jpg")
