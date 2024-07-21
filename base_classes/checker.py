from config import database_path

class Checker:
    """
    Класс для проверки указания пути к хранилищу
    """
    @staticmethod
    def _check_exists_db() -> str:
        """
        Метод для проверки существования файла
        :param database: данные БД
        :return: возвращает путь к файлу
        """
        global database_path
        while True:
            try:
                with open(database_path):
                    print(f'Файл {database_path} успешно найден!')
                    return database_path
            except FileNotFoundError:
                print(f'Файл с именем `{database_path}` не найден.')
                database_path = input('Укажите пожалуйста путь к базе данных `Например: db.txt`\n')
