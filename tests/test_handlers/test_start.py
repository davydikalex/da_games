import pytest
from unittest.mock import AsyncMock

from game_sort import start, kb


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    message.from_user.id = 10
    await start(message)
    message.answer.assert_called_once_with('Привет, '
                                           'я Игровой бот. Выбери игру',
                                           reply_markup=kb.games_catalog())
