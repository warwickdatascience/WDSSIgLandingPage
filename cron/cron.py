from dotenv import load_dotenv
import os
from instagram_puller import InstagramPuller

load_dotenv()

INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
DATA_PATH = os.getenv("DATA_PATH")
LOG_PATH = os.getenv("LOG_PATH")

puller = InstagramPuller(INSTAGRAM_ACCESS_TOKEN, DATA_PATH, LOG_PATH)
puller.set_data()
