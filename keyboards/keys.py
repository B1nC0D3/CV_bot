from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

ABOUT_ME_KEYS = (KeyboardButton(text='Общее представление'),
                 KeyboardButton(text='О хобби'))

PHOTOS_KEYS = (KeyboardButton(text='Последнее селфи'),
               KeyboardButton(text='Фото со школы'))

VOICES_KEYS = (KeyboardButton(text='О GPT'),
               KeyboardButton(text='Разница между SQL и NoSQL'),
               KeyboardButton(text='Про первую любовь'))

KEYBOARDS_VALUES = {
    'StateMenu:about_me': ABOUT_ME_KEYS,
    'StateMenu:photos': PHOTOS_KEYS,
    'StateMenu:voices': VOICES_KEYS
}


async def get_keyboard(state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keys_key = await state.get_state()
    keys = KEYBOARDS_VALUES.get(keys_key)

    keyboard.add(*keys)
    keyboard.add(KeyboardButton(text='Назад'))
    return keyboard


