from state.strawberry import StrState
from aiogram import types
from aiogram import Dispatcher
from additions.keyboard import StrawberryGame
import random
from gamer.strawberry import Gamer
from database.strawberry import StrDB

db = StrDB()
kb = StrawberryGame()


def strawberry_pint_count(count):
    count5 = count // 5
    count_ost = count % 5
    pretty_print = '🍓 🍓 🍓 🍓 🍓\n' * count5
    if count_ost != 0:
        pretty_print += '🍓 ' * count_ost
        pretty_print += '\n'

    return pretty_print


async def start_game(message: types.Message):
    """Старт игры"""
    await message.answer('Игра Клубника коня', reply_markup=kb.start_games())
    if not db.check_reg(str(message.from_user.id)):
        db.create_record_table(str(message.from_user.id), 0)
    await StrState.update_state(message, StrState.START_GAME)


async def begin(message: types.Message):
    """Ожидание команд от зарегистрированного пользователя"""
    if message.text == "Начать":
        await run_game(message)
    if message.text == "Правила":
        await rules(message)
    if message.text == 'Статистика':
        await statistics(message)
    if message.text == 'Выход':
        await exit_game(message)


async def exit_game(message: types.Message):
    await message.answer('Вы в главном меню', reply_markup=kb.games_catalog())
    await StrState.update_state(message, StrState.MAIN_MENU)


async def statistics(message: types.Message):
    gamer = Gamer(message.from_user.id)
    stat = gamer.print_stat()
    await message.answer(f'Победы: {stat[0]}\n'
                         f'Поражения: {stat[1]}')


async def rules(message: types.Message):
    await message.answer('Правила:\n'
                         'Выбирай начальное количество клубничек🍓.\n'
                         'Далее по очереди убираете по 1-3 клубнички.\n'
                         'Проиграл тот кто забрал последнюю клубничку')


async def run_game(message: types.Message):
    await message.answer('Введите количество 🍓 '
                         'с которого начнем: от 20 до 30:',
                         reply_markup=kb.remove_keyboard())
    await StrState.update_state(message, StrState.FIRST_STEP)


async def first_step(message: types.Message):
    """Первый ход"""
    if message.text.isnumeric() and \
            (int(message.text) >= 20) and \
            (int(message.text) <= 30):
        gamer = Gamer(message.from_user.id)
        gamer.set_strawberry_count(int(message.text))
        pretty_print = strawberry_pint_count(gamer.strawberry_count)
        await message.answer(f'{pretty_print}\n'
                             f'Ваш выбор', reply_markup=kb.games())
        await StrState.update_state(message, StrState.GAME_STEP)
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
        pretty_print = strawberry_pint_count(gamer.strawberry_count)
        saf = {1: 'у', 2: 'и', 3: 'и'}
        await message.answer(f'Отлично, а я уберу {a} клубничк{saf[a]}')
        if not gamer.strawberry_count == 1:
            await message.answer(f'{pretty_print}\n'
                                 f'Ваш выбор', reply_markup=kb.games())
        else:
            await message.answer(f'{pretty_print}\n'
                                 f'Ваш выбор',
                                 reply_markup=kb.games(
                                     count=gamer.strawberry_count))
            await StrState.update_state(message, StrState.FINAL_GAME)
    else:
        await message.answer('Поздравляю с победой 🍓🧠🥳',
                             reply_markup=kb.start_games())
        await StrState.update_state(message, StrState.START_GAME)
        gamer.update_strawberry_count(0)
        gamer.update_stat()


async def the_end(message: types.Message):
    gamer = Gamer(message.from_user.id)
    if message.text == '🍓':
        await message.answer('В этот раз удача не на твоей стороне😈😈😈',
                             reply_markup=kb.start_games())
        await StrState.update_state(message, StrState.START_GAME)
    gamer.set_strawberry_count(0)
    gamer.update_stat(win=False)


def register_handler_game1(dispatcher: Dispatcher):
    # Хендлеры для первой игры
    dispatcher.register_message_handler(begin,
                                        state=StrState.START_GAME)
    dispatcher.register_message_handler(first_step,
                                        state=StrState.FIRST_STEP)
    dispatcher.register_message_handler(next_step_reply,
                                        state=StrState.GAME_STEP)
    dispatcher.register_message_handler(the_end,
                                        state=StrState.FINAL_GAME)
