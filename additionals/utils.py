class Utils:
    def get_last_id(self, database: str) -> int:
        """
        Метод для получения последнего id из БД
        :param database: данные БД
        :return: последний id из БД
        """
        with open(database, 'r', encoding='utf-8') as db:
            return len(db.readlines()) if db else None


    def check_id(self, id: int, database: str) -> None:
        """
        Метод для проверки корректности введенного id
        :param id: введенный id
        :param database: данные БД
        :return: вызывается исключение с пояснениями ошибки
        """
        exists_id: list[int] = [x for x in range(1, self.get_last_id(database) + 1)]
        if id not in exists_id:
            raise IndexError(f'Объекта с таким ID не найдено, укажите доступные [{exists_id[0]}...{exists_id[-1]}]')


    def get_first_to_last_id(self, database: str) -> tuple[int, int]:
        """
        Метод для вывода списка всех доступных id из БД
        :param database: данные из БД
        :return: возвращает кортеж с первым и последним элементом доступных id в БД
        """
        ids: list[int] = [x for x in range(1, self.get_last_id(database) + 1)]
        return ids[0], ids[-1]


    def get_status(self, status_id: int) -> str:
        """
        Метод для получения статуса книги
        :param status_id: указывается id книги
        :return: возвращает стутус книги в виде `str`
        """
        return ('выдана', 'в наличии')[status_id]

    @staticmethod
    def space_cls() -> None:
        """
        Метод для добавления пустых строк в консольное меню (вместо cls...)
        """
        print(*('\n' for _ in range(30)))