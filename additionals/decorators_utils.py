def print_table(func):
    """
    Декоратор для оборачивания данных в таблицу
    """
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if data is None:
            return

        print(f"{'ID':<5} | {'Title':<20} | {'Author':<20} | {'Year':<5} | {'Status':<9}"
              f"\n{'-' * 71}") # шапка таблицы

        print(*(f"{row['id']:<5} | {row['title']:<20} | {row['author']:<20} | {row['year']:<5} | {row['status']:<9}"
              for row in data), sep='\n') # основные данные

    return wrapper