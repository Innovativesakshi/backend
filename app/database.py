from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "hrms_lite")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

async def get_database():
    return db
