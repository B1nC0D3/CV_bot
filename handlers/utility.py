from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message


async def start_message(msg: Message):
    await msg.reply('Привет! Это бот для знакомства со мной, то есть с @B1nC0D3.'
                    'Выбери интересующий раздел')


async def reset_state(msg: Message, state: FSMContext):
    await state.finish()
    await msg.reply('Вы вернулись в главное меню!')


def register_utility_handlers(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(reset_state, commands=['cancel'], state='*')
