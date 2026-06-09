from motor.motor_asyncio import AsyncIOMotorClient
from config import DB_URL, DB_NAME
from logging import getLogger

LOGGER = getLogger(__name__)

MEDIA_CACHE = set()


class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.media = None

    async def connect(self):
        try:
            self.client = AsyncIOMotorClient(DB_URL)

            self.db = self.client[DB_NAME]

            self.media = self.db.media

            LOGGER.info("Connected To MongoDB")

        except Exception as e:
            LOGGER.error(f"Mongo Connection Error : {e}")

    async def load_cache(self):

        MEDIA_CACHE.clear()

        count = 0

        async for doc in self.media.find(
            {},
            {"_id": 1}
        ):
            MEDIA_CACHE.add(doc["_id"])
            count += 1

        LOGGER.info(
            f"Loaded {count} Media IDs Into Cache"
        )

        return count

    async def add_media(
        self,
        uid,
        chat_id,
        message_id,
        media_type
    ):

        if uid in MEDIA_CACHE:
            return False

        MEDIA_CACHE.add(uid)

        await self.media.insert_one(
            {
                "_id": uid,
                "chat_id": chat_id,
                "message_id": message_id,
                "media_type": media_type
            }
        )

        return True

    async def is_duplicate(self, uid):

        return uid in MEDIA_CACHE

    async def total_media(self):

        return len(MEDIA_CACHE)


db = Database()
