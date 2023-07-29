from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from keyboards.utility_keys import start_keyboard
from aiogram.dispatcher import FSMContext
from states.main_menu import StateMenu
from keyboards.keys import get_keyboard
from messages import NOT_FOUND_MESSAGE

STATES = {
    'Обо мне': StateMenu.about_me,
    'Войсы': StateMenu.voices,
    'Фото': StateMenu.photo
}


async def start_message(msg: Message):
    await msg.reply('Привет! Это бот для знакомства со мной(@B1nC0D3).\n'
                    'Выбери интересующий раздел:',
                    reply_markup=start_keyboard)


async def reset_state(msg: Message, state: FSMContext):
    await state.finish()
    await msg.reply('Вы вернулись в главное меню!',
                    reply_markup=start_keyboard)


async def get_menu_for_module(msg: Message, state: FSMContext):
    user_state = STATES.get(msg.text)
    if not user_state:
        await msg.answer(NOT_FOUND_MESSAGE)
        return
    await state.set_state(user_state)
    keyboard = await get_keyboard(state)
    await msg.answer('Выбери интересующую тему:',
                     reply_markup=keyboard)


async def not_found_command(msg: Message):
    await msg.answer(NOT_FOUND_MESSAGE)


def register_utility(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(reset_state,
                                Text(equals='Назад', ignore_case=True),
                                state='*')
    dp.register_message_handler(get_menu_for_module)
    dp.register_message_handler(not_found_command, state='*')