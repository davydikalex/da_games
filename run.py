from time import sleep

from aiogram.utils import executor
from config.config import dp
from database.database import DataBase

import game_sort
import games.strawberry.game

db = DataBase()
games.strawberry.game.register_handler_game1(dp)
game_sort.register_handler_game_sort(dp)


async def shutdown(dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


async def on_startup(_):
    sleep(10)
    db.create_table()


if __name__ == "__main__":
    """Запуск бота"""
executor.start_polling(dp, on_startup=on_startup, on_shutdown=shutdown, skip_updates=True)
