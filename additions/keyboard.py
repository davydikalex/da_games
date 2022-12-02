from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


class Btn:
    """Класс кнопок"""
    strawberry = KeyboardButton("Гнилая клубника")
    statistics = KeyboardButton("Статистика")
    rules = KeyboardButton("Правила")
    start = KeyboardButton('Начать')
    exit_btn = KeyboardButton('Выход')

    def games_catalog(self):
        """Клавиатура выбора игр"""
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(self.strawberry)
        return markup

    def start_games(self):
        """Клавиатура игры"""
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(self.start)
        markup.row(self.rules, self.statistics)
        markup.row(self.exit_btn)
        return markup

    @staticmethod
    def remove_keyboard():
        """Удаление клавиатуры"""
        return ReplyKeyboardRemove()


class StrawberryGame(Btn):
    """Класс кнопок игры про клубничку"""

    def games(self, count=3):
        """Создание клавиатуры для игры"""
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(count):
            markup.add(KeyboardButton("🍓" * (i + 1)))
        return markup
