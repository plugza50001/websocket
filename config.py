# config.py
import os

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "cpe1234")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "machine_db"
COLLECTION_NAME = "machine_data"
