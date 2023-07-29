from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from states.main_menu import StateMenu
from settings import LAST_PHOTO, SCHOOL_PHOTO
from aiogram.types import InputFile


async def last_photo(msg: Message):
    # Берем уже существующий класс от библиотеки, вместо того чтобы городить работу с файлом
    await msg.answer_photo(InputFile(LAST_PHOTO),
                           caption='Я решил быть честным и '
                                   'действительно отправил последнее фото XD')


async def school_photo(msg: Message):
    await msg.answer_photo(InputFile(SCHOOL_PHOTO),
                           caption='Не смог найти фото со школы, так что держи фото из колледжа')


def register_photos(dp: Dispatcher):
    dp.register_message_handler(last_photo,
                                Text(equals='Последнее селфи', ignore_case=True),
                                state=StateMenu.photos)
    dp.register_message_handler(school_photo,
                                Text(equals='Фото со школы', ignore_case=True),
                                state=StateMenu.photos)
