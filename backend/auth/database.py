from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("MONGO_URI environment variable is not set.")

client = MongoClient(mongo_uri)

db = client["multi_agent_ai"]

users_collection = db["users"]

conversations_collection = db["conversations"]