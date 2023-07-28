from aiogram import Dispatcher
from aiogram.types import Message


async def about_me(msg: Message):
    await msg.reply('its working')


def register_about_me(dp: Dispatcher):
    dp.register_message_handler(about_me,
                                commands=['about_me'])
