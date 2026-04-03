from pymongo import MongoClient
from app.core.config import settings

def get_database():
    client = MongoClient(settings.database_url)
    db = client.get_default_database()
    print("Connected to MongoDB database:", db.name)
    try:
        yield db
    finally:
        client.close()