from aiogram.dispatcher.filters.state import State, StatesGroup


class StateMenu(StatesGroup):
    photo = State()
    voices = State()
    about_me = State()
