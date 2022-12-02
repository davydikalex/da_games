from database.strawberry import StrDB

db = StrDB()


class Gamer:
    def __init__(self, chat_id):
        """Объявление игрока"""
        self.chat_id = str(chat_id)
        self.strawberry_count = db.check_strawberry_count(str(chat_id))

    def update_strawberry_count(self, count):
        """Изменение количества клубничек"""
        self.strawberry_count += count
        db.update_strawberry_count(self.strawberry_count, self.chat_id)

    def set_strawberry_count(self, count):
        """Установка количества клубничек"""
        self.strawberry_count = count
        db.update_strawberry_count(count, self.chat_id)

    def update_stat(self, win=True):
        """Добавление в статистику победы или поражения"""
        if win:
            db.update_stat_win(self.chat_id)
        else:
            db.update_stat_lose(self.chat_id)

    def print_stat(self):
        """Возвращение статистики"""
        return db.statistics(self.chat_id)


