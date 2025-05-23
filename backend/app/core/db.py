from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

client = MongoClient(os.getenv("MONGO_URI"))
db = client["study_assistant"]
