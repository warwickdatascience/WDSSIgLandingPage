from dotenv import load_dotenv
import os
from instagram_puller import InstagramPuller
import logging

load_dotenv()

INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
DATA_PATH = os.getenv("DATA_PATH")
LOG_PATH = os.getenv("LOG_PATH")

# try to set up the logger - if LOG_PATH not present, it will open at
# the current path
logger = logging.getLogger(__name__)

f_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

if os.path.isdir(LOG_PATH):
    f_handler = logging.FileHandler(f"{LOG_PATH}/instagram_puller.log")
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
else:
    # it will default to log at current directory - we might need to
    # change this
    f_handler = logging.FileHandler("./instagram_puller.log")
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.error(f"Could not find logging directory {LOG_PATH}")

try:
    puller = InstagramPuller(INSTAGRAM_ACCESS_TOKEN, DATA_PATH)
    puller.set_data()
except Exception as e:
    logger.error(e)
