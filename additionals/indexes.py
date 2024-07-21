def reindex(db: str, data: list) -> str:
    """
    Метод для упорядочивания всех id после удаления записи
    :param data: данные из БД
    :return:
    """
    if not data:
        return

    sort_data = sorted(data, key=lambda x: int(x['id']))

    with open(db, 'w+', encoding='utf-8') as db:
        first_id = 1

        for row in sort_data:
            row['id'] = first_id
            db.write(f"id={row['id']},title={row['title']},author={row['author']},year={row['year']},status={row['status']}\n")
            first_id += 1

        db.seek(0)
        return db.read()