import logging
from logging.handlers import RotatingFileHandler

API_ID = 22724444 
API_HASH = "d88e1dcdd8c5601832784adfc580442d"
BOT_TOKEN = "7813937360:AAFmy_0qxKw1F7RRDixPCEQoZjIyEgF09TI"

ADMINS = [7852142757 , 7838009892, 6573328336]

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            'log.txt',
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("aiohttp").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
