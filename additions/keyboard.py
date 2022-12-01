from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove


class Btn:
    """Класс кнопок"""
    strawberry = KeyboardButton("Гнилая клубника")
    statistics = KeyboardButton("Статистика")
    rules = KeyboardButton("Правила")
    start = KeyboardButton('Начать')

    def games(self):
        """Создание клавиатуры для регистрации"""
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(self.strawberry)
        return markup

    def start_games(self):
        """Создание клавиатуры для регистрации"""
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(self.start)
        markup.row(self.rules, self.statistics)
        return markup

    @staticmethod
    def remove_keyboard():
        return ReplyKeyboardRemove()


class StrawberryGame(Btn):
    """Класс кнопок игры про клубничку"""
    surrender = KeyboardButton("Cдаться")

    def games(self, count=3):
        """Создание клавиатуры для игры"""
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(count):
            markup.add(KeyboardButton("🍓" * (i + 1)))
        markup.row(self.surrender)
        return markup
