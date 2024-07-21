def str_to_dict(db: str) -> tuple[dict[str, int | str]]:
    """
    Преобразует список строк, где каждая строка представляет собой набор пар ключ=значение, разделенных запятыми,
    в список словарей
    :param db: список строк, где каждая строка содержит пары ключ=значение
    :return: кортеж словарей, преобразованных str -> dict из БД
    """
    if not db:
        return tuple()

    nested_list = tuple(row.split(',') for row in db.strip().split('\n'))
    dct_lst = list()

    for row in nested_list:
        dct = {}
        for pair in row:
            key, value = pair.split('=')
            dct[key] = int(value) if value.isdigit() else value

        dct_lst.append(dct)
    return tuple(dct_lst)