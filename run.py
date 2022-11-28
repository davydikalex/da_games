from aiogram.utils import executor
from config.config import get
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import game_sort
import strawberry.game


bot = Bot(get('TOKEN'))
dp = Dispatcher(bot=bot, storage=MemoryStorage())

strawberry.game.register_handler_game1(dp)
game_sort.register_handler_game_sort(dp)


async def shutdown(dispatcher=dp):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == "__main__":
    """Запуск бота"""
executor.start_polling(dp, on_shutdown=shutdown, skip_updates=True)
