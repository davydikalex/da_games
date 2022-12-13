import unittest

from aiogram_unittest import Requester
from aiogram_unittest.handler import MessageHandler
from aiogram_unittest.types.dataset import MESSAGE

from game_sort import start, main_menu


class TestBot(unittest.IsolatedAsyncioTestCase):
    async def test_echo(self):
        requester = Requester(
            request_handler=MessageHandler(start,
                                           commands=["start"]))

        message = MESSAGE.as_object(text="/start")
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, "Привет, я Игровой бот. Выбери игру")

    async def test_message_handler_with_state(self):
        requester = Requester(request_handler=MessageHandler(main_menu))

        message = MESSAGE.as_object(text="Гнилая клубника")
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        print(calls.send_message.fetchone().reply_markup['keyboard'])
        self.assertEqual(answer_message, "Игра Клубника коня")
