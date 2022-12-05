import psycopg2
from psycopg2 import OperationalError


class DataBase:
    """Основной класс для работы с БД"""
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
            print(f'<h2>Соединение было </h2>')
        except OperationalError as error:
            print(f'<h2>Ошибка подключения к БД: {error} </h2>')

    def create_table(self):
        """Создание таблицы strawberry_count
        """
        query = """
        CREATE TABLE users  
        (chat_id TEXT NOT NULL,
        strawberry_count INT NOT NULL,
        win INT,
        lose INT)
        """
        self.execute_query(query)
        print('TABLE CREATE')
