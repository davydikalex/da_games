from database.database import DataBase


class StrDB(DataBase):
    """Работа с базой данных для игры 'Клубничка'"""

    def create_record_table(self, *args):
        """Добавление новой записи в базу данных"""
        query = """
        INSERT INTO
            users (chat_id, strawberry_count, win, lose)
        VALUES
            (%s, %s, 0, 0)
        """
        self.execute_query(query, *args)

    def check_strawberry_count(self, chatID):
        """Проверка strawberry_count
        Возвращает количество клубничек"""
        query = """
        SELECT
            strawberry_count
        FROM
            users
        WHERE
            chat_id = %s
        """
        return self.execute_query(query, chatID, read=True)[0][0]

    def update_strawberry_count(self, strawberry_count, chatID):
        """Редактирование количества клубничек"""
        query = """
        UPDATE
          users
        SET
          strawberry_count = %s
        WHERE
          chat_id = %s
        """
        self.execute_query(query, strawberry_count, chatID)

    def check_reg(self, chatID):
        """Проверка существования chat_id"""
        query = """
        SELECT
            chat_id
        FROM
            users
        """
        chat_id = self.execute_query(query, read=True)
        for i in chat_id:
            for j in i:
                if j == chatID:
                    return True
        return False

    def update_stat_win(self, chatID):
        """Добавление победы"""
        query = """
        SELECT
            win
        FROM
            users
        WHERE
            chat_id = %s
        """
        win = self.execute_query(query, chatID, read=True)[0][0] + 1
        query = """
        UPDATE
          users
        SET
          win = %s
        WHERE
          chat_id = %s
        """
        return self.execute_query(query, win, chatID)

    def update_stat_lose(self, chatID):
        """Добавление поражения"""
        query = """
        SELECT
            lose
        FROM
            users
        WHERE
            chat_id = %s
        """
        lose = self.execute_query(query, chatID, read=True)[0][0] + 1
        query = """
        UPDATE
          users
        SET
          lose = %s
        WHERE
          chat_id = %s
        """
        return self.execute_query(query, lose, chatID)

    def statistics(self, chatID):
        """Вычитка статистики.
        Возвращает количество побед и поражений"""
        query = """
        SELECT
            win, lose
        FROM
            users
        WHERE
            chat_id = %s
        """
        statistics = self.execute_query(query, chatID, read=True)[0]
        return statistics
