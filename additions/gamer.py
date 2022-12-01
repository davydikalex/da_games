from database.database import DataBase

db = DataBase()


class Gamer:
    def __init__(self, chat_id):
        self.chat_id = str(chat_id)
        self.strawberry_count = db.check_strawberry_count(str(chat_id))  # TODO Брать из бд по чат_ид

    def update_strawberry_count(self, count):
        self.strawberry_count += count
        db.update_strawberry_count(self.strawberry_count, self.chat_id)

    def set_strawberry_count(self, count):
        self.strawberry_count = count
        db.update_strawberry_count(count, self.chat_id)

    def update_stat(self, win=True):
        if win:
            db.update_stat_win(self.chat_id)
        else:
            db.update_stat_lose(self.chat_id)