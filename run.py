from aiogram.utils import executor
from config.config import dp

import game_sort
import games.strawberry.game

games.strawberry.game.register_handler_game1(dp)
game_sort.register_handler_game_sort(dp)


async def shutdown(dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == "__main__":
    """Запуск бота"""
executor.start_polling(dp, on_shutdown=shutdown, skip_updates=True)
