from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()



class Settings():
    TOKEN = os.environ.get("TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    UPSTASH_VECTOR_REST_TOKEN = os.environ.get("UPSTASH_VECTOR_REST_TOKEN")
    UPSTASH_VECTOR_REST_URL = os.environ.get("UPSTASH_VECTOR_REST_URL")


# config = get_config()

@lru_cache()
def get_config():
    return Settings()
