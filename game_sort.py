from aiogram import types
from aiogram import Dispatcher

from additions.keyboard import Btn
from additions.states_game import States
import strawberry.game as sg1
from database.database import DataBase

db = DataBase()

kb = Btn()


async def start(message: types.Message):
    """Обработка команды старт"""
    await message.answer('Привет, я Игровой бот. Выбери игру', reply_markup=kb.games())
    if not db.check_reg(str(message.from_user.id)):
        db.create_record_table(str(message.from_user.id), 0)
    await States.update_state(message, States.MAIN_MENU)


async def main_menu(message: types.Message):
    """Обработка главного меню игры"""

    if message.text == "Гнилая клубника":
        await sg1.start_game(message)
    if message.text == "Статистика":
        await message.answer(f'Вот ваша статистика которую я соберу с бд по меседжИД')


def register_handler_game_sort(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start, commands='start')
    dispatcher.register_message_handler(main_menu, state=States.MAIN_MENU)
