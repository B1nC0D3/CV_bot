from aiogram import Bot, Dispatcher
from settings import TG_TOKEN
from handlers.about_me import register_about_me
from handlers.utility import register_utility
from handlers.voices import register_voices
from handlers.photos import register_photos
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
import asyncio

# Юзаю лист из-за какой-то специфики работы функции, глубоко не лез.
BOT_COMMANDS = [
    BotCommand(command='/start', description='Запуск бота'),
    BotCommand(command='/tech_details', description='Технические детали и ссылка на репозиторий')]


async def set_commands(bot: Bot):
    await bot.set_my_commands(BOT_COMMANDS)


async def main():
    # Сетапим бота
    bot = Bot(TG_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрируем хэндлеры, утилити обязательно последними
    register_about_me(dp)
    register_photos(dp)
    register_voices(dp)
    register_utility(dp)

    # Стартуем бота через пулинг, так как мой хостинг не может в вебхуки )
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
