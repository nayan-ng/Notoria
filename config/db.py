from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

conn = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)
