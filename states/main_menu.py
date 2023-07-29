from aiogram.dispatcher.filters.state import State, StatesGroup


class StateMenu(StatesGroup):
    photos = State()
    voices = State()
    about_me = State()
