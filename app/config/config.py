from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

API_URL = "https://api.open-meteo.com/v1/forecast"
