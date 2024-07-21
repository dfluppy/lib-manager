from .library_manager import Library, database_path
from additionals.utils import Utils


class Menu:
    def console_menu(self) -> None:
        """
        Основной функционал меню программа. Пользователь имеет возможность использовать следующие функции интерфейса:
        [Insert / Delete / Update / Read]
        :return: None
        """

        lib: Library = Library()
        utils: Utils = Utils()

        while True:
            print("\n▐░░░░░░░ МЕНЮ ░░░░░░░░▌")
            print("[1] Добавить книгу")
            print("[2] Удалить книгу")
            print("[3] Обновить статус книги")
            print("[4] Вывести все книги")
            print("[5] Выйти")

            choice: str = input("\nВыберите действие (1-5): ")

            match choice:
                case '1':
                    utils.space_cls()
                    try:
                        title = input("Введите название книги: ")
                        if not isinstance(title, str) or not title:
                            raise ValueError('Название книги не может быть пустым, укажите название!')

                        author = input("Введите автора книги: ")
                        if not isinstance(author, str) or not author:
                            raise ValueError('Поле автора не может быть пустым, укажите автора!')

                        year = int(input("Введите год издания книги: "))
                        if not isinstance(author, str) or len(str(year)) != 4 or not year:
                            raise ValueError('Неверно указан год [формат : YYYY]')

                        status = utils.get_status(int(input("Укажите статус книги (число) [0: выдана / 1: в наличии]: ")))
                        print(status)
                        if not isinstance(author, str) or not status:
                            raise ValueError('Статус может быть только [0: выдана / 1: в наличии]!')

                        lib.add_book(title, author, year, status)

                    except ValueError as ve:
                        print('Ошибка значения: ', ve)
                    except TypeError as te:
                        print('Ошибка типа: ', te)
                    except Exception as e:
                        print('Ошибка: ', e)

                case '2':
                    utils.space_cls()
                    try:
                        first_id: int
                        last_id: int

                        first_id, last_id = utils.get_first_to_last_id(database_path)
                        id = int(input(f"Введите ID книги, которую необходимо удалить [{first_id}...{last_id}]: "))
                        utils.check_id(id, database_path)

                        lib.remove_book(id)

                    except IndexError as ie:
                        print('Ошибка индекса: ', ie)
                    except Exception as e:
                        print('Ошибка: ', e)

                case '3':
                    utils.space_cls()
                    try:
                        first_id: int
                        last_id: int

                        first_id, last_id = utils.get_first_to_last_id(database_path)
                        id = int(input(f"Введите ID книги [{first_id}...{last_id}]: "))
                        utils.check_id(id, database_path)

                        status = utils.get_status(int(input("Укажите статус книги (число) [0: выдана / 1: в наличии]: ")))
                        if not isinstance(status, str) or not status:
                            raise ValueError('Статус может быть только [0: выдана / 1: в наличии]!')

                        lib.update_status(id, status)

                    except Exception as e:
                        print('Ошибка: ', e)

                case '4':
                    utils.space_cls()
                    try:
                        lib.get_all_books()
                    except Exception as e:
                        print('Ошибка: ', e)
                case '5':
                    print("Завершение программы.")
                    break

                case _:
                    print("Такого варианта не существует. Выберите действие от 1 до 5")