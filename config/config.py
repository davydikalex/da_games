import configparser
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


def get(option: str, section='general'):
    """Возвращает значение опции
        :param option: имя опции
        :param section: имя секции
        """
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    value = config.get(section, option)
    return value


bot = Bot(get('TOKEN'))  # Получаем токен бота из конфига
dp = Dispatcher(bot=bot, storage=MemoryStorage())  # Объявляем диспетчер
