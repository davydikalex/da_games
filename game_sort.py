from aiogram import types
from additions.keyboard import Btn
from additions.state import States
import strawberry.game1 as sg1
from aiogram import Dispatcher

kb = Btn()


async def start(message: types.Message):
    """Обработка команды старт"""
    await message.answer('Привет, я Игровой бот. Выбери игру', reply_markup=kb.games())
    await States.update_state(message, States.STATE_1)


async def main_menu(message: types.Message):
    """Обработка главного меню игры"""

    if message.text == "Гнилая клубника":
        await sg1.start_game(message)
    if message.text == "Статистика":
        await message.answer(f'Вот ваша статистика которую я соберу с бд по меседжИД')


def register_handler_game_sort(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start, commands='start')
    dispatcher.register_message_handler(main_menu, state=States.STATE_1)
