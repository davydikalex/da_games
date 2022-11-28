from aiogram.utils import executor
from config.config import get
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from additions.state import States
# from database import DataBase

import game_sort
import strawberry.game1


bot = Bot(get('TOKEN'))
dp = Dispatcher(bot=bot, storage=MemoryStorage())

# async def on_startup(_):
#     users = DataBase.cursor.execute('SELECT user_id, user_state, user_inputname FROM Users')
#     users = users.fetchall()
#     for user in users:
#         user_id = user[0]
#         user_state = user[1]
#         user_inputname = user[2]
#         if user_inputname:
#             await States.set_state(user_id=user_id, user_state=user_state)
#         else:
#             await States.set_state(user_id=user_id, user_state='STATE_REGISTERED')

strawberry.game1.register_handler_game1(dp)
game_sort.register_handler_game_sort(dp)


async def shutdown(dispatcher=dp):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == "__main__":
    """Запуск бота"""
executor.start_polling(dp, on_shutdown=shutdown, skip_updates=True)
