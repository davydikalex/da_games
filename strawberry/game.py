from aiogram import types
from aiogram import Dispatcher

import random


from additions.state import States
from additions.keyboard import StrawberryGame

kb = StrawberryGame()


async def start_game(message: types.Message):
    """Старт игры"""
    await message.answer('Игра Клубника коня', reply_markup=kb.start_games())
    await States.update_state(message, States.START_GAME)


async def begin(message: types.Message):
    """Ожидание команд от зарегистрированного пользователя"""
    if message.text == "Начать":
        await run_game(message)
    # if message.text == "Правила":
    #     await members(message)
    # if message.text == 'Статистика':
    #     await statistics(message)


async def run_game(message: types.Message):
    await message.answer('Введите количество с которого начнем: 20-30', reply_markup=kb.remove_keyboard())
    await States.update_state(message, States.FIRST_STEP)


async def first_step(message: types.Message):
    """Первый ход"""
    if message.text.isnumeric() and (int(message.text) >= 20) and (int(message.text) <= 30):
        message.set_strawberry_count(int(message.text))
        pretty_print = '🍓 ' * message.strawberry_count
        await message.answer(f'{pretty_print}'
                           f'Ваш выбор', reply_markup=kb.games())
        await States.update_state(message, States.GAME_STEP)
    else:
        await message.answer('Введите количество с которого начнем: 20-30')


async def next_step_reply(message: types.Message):
    """Ход игрока"""
    if message.text == '🍓':
        message.strawberry_count -= 1
        await next_step(message)
    if message.text == '🍓🍓':
        message.strawberry_count -= 2
        await next_step(message)
    if message.text == '🍓🍓🍓':
        message.strawberry_count -= 3
        await next_step(message)


async def next_step(message: types.Message):
    if not await exit_game():
        if (message.strawberry_count - 1) % 4 == 0:
            a = random.randint(1, 3)
        else:
            a = (message.strawberry_count - 1) % 4
        message.set_strawberry_count(message.strawberry_count - a)
        pretty_print = '🍓 ' * message.strawberry_count
        saf = {1: 'у', 2: 'и', 3: 'и'}
        await message.answer(f'Отлично, а я уберу {a} клубничк{saf[a]}')
        if not await exit_game(message):
            await message.answer(f'{pretty_print}'
                               f'Ваш выбор', reply_markup=kb.games())
        else:
            await message.answer(f'{pretty_print}'
                               f'Ваш выбор', reply_markup=kb.games(count=message.strawberry_count))
            await States.update_state(message, States.FINAL_GAME)
    else:
        await message.answer(f'Хорош, я проиграл', reply_markup=kb.remove_keyboard())


async def exit_game(message: types.Message):
    if message.strawberry_count == 1:
        return True
    return False


async def the_end(message: types.Message):
    if message.text == '🍓':
        await message.answer(f'Хорош, ты проиграл', reply_markup=kb.remove_keyboard())


def register_handler_game1(dispatcher: Dispatcher):
    # Хендлеры для первой игры
    dispatcher.register_message_handler(begin, state=States.START_GAME)
    dispatcher.register_message_handler(first_step, state=States.FIRST_STEP)
    dispatcher.register_message_handler(next_step_reply, state=States.GAME_STEP)
    dispatcher.register_message_handler(the_end, state=States.FINAL_GAME)