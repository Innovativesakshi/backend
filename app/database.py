from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

import certifi

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "hrms_lite")

# Add tlsCAFile=certifi.where() to fix SSL handshake errors on cloud platforms/Render
client = AsyncIOMotorClient(MONGO_URI, tlsCAFile=certifi.where())
db = client[DB_NAME]

async def get_database():
    return db
