from aiogram.fsm.state import StatesGroup, State


class Chat(StatesGroup):
    text = State()
    wait = State()


class Image(StatesGroup):
    text = State()
    wait = State()


class Newsletter(StatesGroup):
    message = State()
