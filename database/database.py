import psycopg2
from psycopg2 import OperationalError


class DataBase:
    connect = None

    @staticmethod
    def execute_query(query, *args, read=False):
        try:
            connect = psycopg2.connect(
                database='postgres',
                user='postgres',
                password='1478',
                host='localhost',
                port='5432'
            )
            cursor = connect.cursor()
            if read:
                cursor.execute(query, args)
                return cursor.fetchall()
            else:
                cursor.execute(query, args)
                connect.commit()
                connect.close()
        except OperationalError as error:
            print(f'<h2>Ошибка подключения к БД: {error} </h2>')

    def create_record_table(self, *args):
        """Добавление записи в базу данных"""
        create_users = """
        INSERT INTO 
            users (chat_id, strawberry_count, win, lose) 
        VALUES 
            (%s, %s, 0, 0)
        """
        self.execute_query(create_users, *args)

    def read_all_table(self):
        """Чтение всех записей таблицы"""
        select_users = """
        SELECT
            *
        FROM
            users
        """
        a = self.execute_query(select_users, read=True)
        return a

    def check_strawberry_count(self, chatID):
        """Проверка strawberry_count"""
        select_users = """
        SELECT
            strawberry_count
        FROM
            users
        WHERE
            chat_id = %s
        """
        return self.execute_query(select_users, chatID, read=True)[0][0]

    def update_strawberry_count(self, strawberry_count, chatID):
        """Редактирование chat_name"""
        update = """
        UPDATE
          users
        SET
          strawberry_count = %s
        WHERE
          chat_id = %s
        """
        self.execute_query(update, strawberry_count, chatID)

    def check_reg(self, chatID):
        """Проверка уникальности chat_id"""
        select_users = """
        SELECT
            chat_id
        FROM
            users
        """
        chat_id = self.execute_query(select_users, read=True)
        for i in chat_id:
            for j in i:
                if j == chatID:
                    return True
        return False

    def update_stat_win(self, chatID):
        """Добавление победы
        :param chatID
        :param params: win, lose"""
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
        """Добавление поражения"""
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



