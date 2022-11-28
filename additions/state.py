from run import dp
from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):

    MAIN_MENU = State()  # Зарегистрированный пользователь
    START_GAME = State()  # Зарегистрированный пользователь
    FIRST_STEP = State()  # Зарегистрированный пользователь
    GAME_STEP = State()  # Зарегистрированный пользователь
    FINAL_GAME = State()  # Зарегистрированный пользователь

    @staticmethod
    async def update_state(message, argument):
        """Обновление статуса для пользователя
        :param message: Сообщение или callback
        :param argument: Новый state
        """

        state = dp.get_current().current_state(user=message.from_user.id, chat=message.from_user.id)
        await state.set_state(argument)

