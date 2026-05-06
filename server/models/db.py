from pymongo import MongoClient
import os

_client = None

def get_db():
    global _client
    if _client is None:
        uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        _client = MongoClient(uri)
    db_name = os.getenv("MONGO_DB", "learnquiz")
    return _client[db_name]
