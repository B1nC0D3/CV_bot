from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from states.main_menu import StateMenu
from aiogram.types import InputFile
from settings import GPT_VOICE, SQL_VOICE, FIRST_LOVE_VOICE


async def send_gpt_voice(msg: Message):
    await msg.answer_voice(InputFile(GPT_VOICE))


async def send_sql_voice(msg: Message):
    await msg.answer_voice(InputFile(SQL_VOICE))


async def send_first_love_voice(msg: Message):
    await msg.answer_voice(InputFile(FIRST_LOVE_VOICE))


def register_voices(dp: Dispatcher):
    dp.register_message_handler(send_sql_voice,
                                Text(equals='О GPT', ignore_case=True),
                                state=StateMenu.voices)
    dp.register_message_handler(send_sql_voice,
                                Text(equals='Разница между SQL и NoSQL',
                                     ignore_case=True),
                                state=StateMenu.voices)
    dp.register_message_handler(send_first_love_voice,
                                Text(equals='Про первую любовь', ignore_case=True),
                                state=StateMenu.voices)
