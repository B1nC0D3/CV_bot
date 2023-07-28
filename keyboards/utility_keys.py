from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_buttons = (
    KeyboardButton(text='Обо мне'),
    KeyboardButton(text='Войсы'),
    KeyboardButton(text='Фото'),
)

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

start_keyboard.add(*start_buttons)
