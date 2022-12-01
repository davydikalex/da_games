import configparser
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


def get(option: str, section='general'):
    """Возвращает значение опции

        :param option: имя опции
        :param section: имя секции

        | Если опция задана в config вернёт её значение
        | Если нет задана, вернёт None
        """
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    # try:
    value = config.get(section, option)
    # except Exception:
    #     return None
    return value


bot = Bot(get('TOKEN'))
dp = Dispatcher(bot=bot, storage=MemoryStorage())
