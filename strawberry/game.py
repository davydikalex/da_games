from additions.states_game import States
from aiogram import types
from aiogram import Dispatcher
from additions.keyboard import StrawberryGame
import random
from additions.gamer import Gamer

kb = StrawberryGame()


async def start_game(message: types.Message):
    """Старт игры"""
    await message.answer('Игра Клубника коня', reply_markup=kb.start_games())
    await States.update_state(message, States.START_GAME)


async def begin(message: types.Message):
    """Ожидание команд от зарегистрированного пользователя"""
    if message.text == "Начать":
        await run_game(message)
    if message.text == "Правила":
        await rules(message)
    # if message.text == 'Статистика':
    #     await statistics(message)


async def rules(message: types.Message):
    await message.answer('Правила:\n Выбирай начальное количество клубничек🍓. Далее по очереди убираете по 1-3 '
                         'клубнички. Проиграл тот кто забрал последнюю клубничку')


async def run_game(message: types.Message):
    await message.answer('Введите количество 🍓 с которого начнем: от 20 до 30:', reply_markup=kb.remove_keyboard())
    await States.update_state(message, States.FIRST_STEP)


async def first_step(message: types.Message):
    """Первый ход"""
    if message.text.isnumeric() and (int(message.text) >= 20) and (int(message.text) <= 30):
        gamer = Gamer(message.from_user.id)
        gamer.set_strawberry_count(int(message.text))
        pretty_print = '🍓 ' * gamer.strawberry_count
        await message.answer(f'{pretty_print}'
                             f'Ваш выбор', reply_markup=kb.games())
        await States.update_state(message, States.GAME_STEP)
    else:
        await message.answer('Введите количество от 20 до 30')


async def next_step_reply(message: types.Message):
    """Ход игрока"""
    gamer = Gamer(message.from_user.id)
    if message.text == '🍓':
        gamer.update_strawberry_count(-1)
        await next_step(message)
    if message.text == '🍓🍓':
        gamer.update_strawberry_count(-2)
        await next_step(message)
    if message.text == '🍓🍓🍓':
        gamer.update_strawberry_count(-3)
        await next_step(message)


async def next_step(message: types.Message):
    gamer = Gamer(message.from_user.id)
    if not gamer.strawberry_count == 1:
        if (gamer.strawberry_count - 1) % 4 == 0:
            a = random.randint(1, 3)
        else:
            a = (gamer.strawberry_count - 1) % 4
        gamer.update_strawberry_count(-a)
        pretty_print = '🍓 ' * gamer.strawberry_count
        saf = {1: 'у', 2: 'и', 3: 'и'}
        await message.answer(f'Отлично, а я уберу {a} клубничк{saf[a]}')
        if not gamer.strawberry_count == 1:
            await message.answer(f'{pretty_print}'
                                 f'Ваш выбор', reply_markup=kb.games())
        else:
            await message.answer(f'{pretty_print}'
                                 f'Ваш выбор', reply_markup=kb.games(count=gamer.strawberry_count))
            await States.update_state(message, States.FINAL_GAME)
    else:
        await message.answer(f'Хорош, я проиграл', reply_markup=kb.remove_keyboard())
        gamer.update_strawberry_count(0)
        gamer.update_stat()


async def the_end(message: types.Message):
    gamer = Gamer(message.from_user.id)
    if message.text == '🍓':
        await message.answer(f'Хорош, ты проиграл', reply_markup=kb.remove_keyboard())
    gamer.update_strawberry_count(0)
    gamer.update_stat(win=False)


def register_handler_game1(dispatcher: Dispatcher):
    # Хендлеры для первой игры
    dispatcher.register_message_handler(begin, state=States.START_GAME)
    dispatcher.register_message_handler(first_step, state=States.FIRST_STEP)
    dispatcher.register_message_handler(next_step_reply, state=States.GAME_STEP)
    dispatcher.register_message_handler(the_end, state=States.FINAL_GAME)
