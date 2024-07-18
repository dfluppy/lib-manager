def str_to_dict(db: str) -> list[dict[str, int | str]]:
    """
    Преобразует список строк, где каждая строка представляет собой набор пар ключ=значение, разделенных запятыми,
    в список словарей
    :param db: список строк, где каждая строка содержит пары ключ=значение
    :return: список словарей, преобразованных str -> dict из БД
    """
    if not db:
        return

    raw_data = db.strip().split('\n')
    nested_list = []

    for raw in raw_data:
        nested_list.append(raw.split(','))

    dct_lst = []

    for row in nested_list:
        dct = {}
        for pair in row:
            key, value = pair.split('=')

            if value.isdigit():
                value = int(value)
            else:
                value = value

            dct[key] = value

        dct_lst.append(dct)
    return dct_lst