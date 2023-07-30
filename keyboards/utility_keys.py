from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Та же ситуация, что и в keys, но у нас отдельный случай, поэтому решил вынести в отдельный файл
start_buttons = (
    KeyboardButton(text='Обо мне'),
    KeyboardButton(text='Войсы'),
    KeyboardButton(text='Фото'),
)

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

start_keyboard.add(*start_buttons)
