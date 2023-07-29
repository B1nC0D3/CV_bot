from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from messages import ABOUT_ME_GENERAL_MSG, ABOUT_ME_HOBBIES_MESSAGE
from states.main_menu import StateMenu


async def about_me_general(msg: Message):
    await msg.answer(ABOUT_ME_GENERAL_MSG)


async def about_hobbies(msg: Message):
    await msg.answer(ABOUT_ME_HOBBIES_MESSAGE)


def register_about_me(dp: Dispatcher):
    dp.register_message_handler(about_me_general,
                                Text(equals='Общее представление', ignore_case=True),
                                state=StateMenu.about_me)
    dp.register_message_handler(about_hobbies,
                                Text(equals='О хобби', ignore_case=True),
                                state=StateMenu.about_me)
