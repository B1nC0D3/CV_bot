from aiogram import Bot, Dispatcher
from settings import TG_TOKEN
from handlers.about_me import register_about_me
from handlers.utility import register_utility
import asyncio


async def main():
    bot = Bot(TG_TOKEN)
    dp = Dispatcher(bot)

    register_about_me(dp)

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
