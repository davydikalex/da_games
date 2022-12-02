from state.states_game import States
from aiogram.dispatcher.filters.state import State


class StrState(States):
    START_GAME = State()  # Начало игры
    FIRST_STEP = State()  # Первый ход в игре
    GAME_STEP = State()  # Ходы в течении игры
    FINAL_GAME = State()  # Конец игры
