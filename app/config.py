from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()



class Settings():
    TOKEN = os.environ.get("TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")


# config = get_config()

@lru_cache()
def get_config():
    return Settings()

print(get_config().BOT_USERNAME)