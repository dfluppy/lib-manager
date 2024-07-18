from config import database_path
from additionals.converter import str_to_dict
from additionals.utils import get_last_id
from additionals.indexes import reindex
from additionals.decorators_utils import print_table


class Book:
    """
    Класс для описания книг
    """

    __id: int = get_last_id(database_path)

    def __init__(self, title: str, author: str, year: int, status: str):
        Book.__id += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @property
    def get_book_id(self) -> int:
        return self.__id


class Library:
    """
    Интерфейс для управления базой данных библиотеки
    """

    # Проверка на существование БД

    def __check_exists_db(self, database: str) -> bool:
        """
        Метод для проверки существования файла
        :param database: данные БД
        :return: возвращает True если файл/путь найден, False в противном случае
        """

        try:
            with open(database):
                return True
        except FileNotFoundError:
            print(f'Файл с именем `{database}` не найден.')

            path_db = input('Укажите пожалуйста путь к базе данных `Например: db.txt`\n')
            global database_path
            database_path = path_db

    def add_book(self, title: str, author: str, year: int, status: str) -> None:
        """
        Метод добавления новой книги в БД библиотеки
        :param title: название книги
        :param author: автор книги
        :param year: год издания
        :param status: статус
        :return: ничего не возвращает, только добавляет данные если они корректны
        """

        if not self.__check_exists_db(database_path):
            return

        book = Book(title, author, year, status)
        add_data = f'id={book.get_book_id},title={book.title},author={book.author},year={book.year},status={book.status}'
        with open(database_path, 'a', encoding='utf-8') as db:
            db.write(add_data + '\n')

    def remove_book(self, id: int) -> None:
        """
        Метод для удаления книги из БД библиотеки
        :param id: существующий идентификатор книги
        :return: ничего не возвращает, только удаляет книгу по id
        """

        if not self.__check_exists_db(database_path):
            return

        with open(database_path, 'r+', encoding='utf-8') as db:
            lines = db.readlines()
            db.seek(0)
            db.truncate()

            for line in lines:
                if not line.startswith(f'id={id},'):
                    db.write(line)

            db.seek(0)
            reindex_data = reindex(str_to_dict(db.read()))
            str_to_dict(reindex_data)

    def update_status(self, id: int, status: str) -> None:
        """
        Метод для обновления статуса книги
        :param id: существующий идентификатор книги
        :param status: присвоение нового статуса
        :return: ничего не возвращает, только обновляет данные статуса
        """

        if not self.__check_exists_db(database_path):
            return

        with open(database_path, 'r+', encoding='utf-8') as db:
            lines = db.readlines()
            db.seek(0)
            db.truncate()

            for row in lines:
                if row.startswith(f'id={id},'):
                    part = row.strip().split(',')
                    part[4] = f'status={status}'
                    row = ','.join(part) + '\n'
                db.write(row)

    # Вывод всех книг в виде таблицы
    @print_table
    def get_all_books(self) -> list:
        """
        Метод для вывода всех записей из БД
        :return: возвращает список всех записей
        """
        with open(database_path, 'r', encoding='utf-8') as db:
            data_read = db.read()
            reindex_data = reindex(str_to_dict(data_read))
            return str_to_dict(reindex_data)