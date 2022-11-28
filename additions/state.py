from config.config import dp
from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):

    STATE_0 = State()  # Не зарегистрированный пользователь
    STATE_1 = State()  # Зарегистрированный пользователь
    STATE_2 = State()  # Зарегистрированный пользователь
    STATE_3 = State()  # Зарегистрированный пользователь
    STATE_4 = State()  # Зарегистрированный пользователь
    STATE_5 = State()  # Зарегистрированный пользователь

    @staticmethod
    async def update_state(message, argument):
        """Обновление статуса для пользователя
        :param message: Сообщение или callback
        :param argument: Новый state
        """

        state = dp.get_current().current_state(user=message.from_user.id, chat=message.from_user.id)
        print(state.storage.data)
        await state.set_state(argument)
        print(state.storage.data)
        print('_______________________________')
