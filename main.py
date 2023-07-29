from aiogram import Bot, Dispatcher
from settings import TG_TOKEN
from handlers.about_me import register_about_me
from handlers.utility import register_utility
from handlers.voices import register_voices
from handlers.photos import register_photos
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


async def main():
    bot = Bot(TG_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_about_me(dp)
    register_photos(dp)
    register_voices(dp)
    register_utility(dp)

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
