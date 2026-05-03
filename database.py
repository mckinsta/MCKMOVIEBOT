from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URI

client = AsyncIOMotorClient(DATABASE_URI)
db = client["movie_bot"]

movies = db.movies
