"""Small JSON-backed database used by the local application."""

import datetime

from .local_resources import get_local_db, save_local_db


def get_db_item(table_name, key_name, key_value, default_return=None):
    del key_name  # Kept in the public API so existing callbacks need no changes.
    table = get_local_db().get(table_name, {})
    return table.get(key_value, default_return)


def put_db_item(table_name, key_name, key_value, item_name, item_value):
    del key_name
    database = get_local_db()
    table = database.setdefault(table_name, {})
    table[key_value] = {item_name: item_value}
    save_local_db(database)


def update_db_item(table_name, key_name, key_value, item_name, item_value):
    del key_name
    database = get_local_db()
    table = database.setdefault(table_name, {})
    item = table.setdefault(key_value, {})
    item[item_name] = item_value
    save_local_db(database)
    return True


def delete_db_item(table_name, key_name, key_value):
    del key_name
    database = get_local_db()
    table = database.setdefault(table_name, {})
    if key_value not in table:
        return False
    del table[key_value]
    save_local_db(database)
    return True


def update_last_activity(session_id):
    return update_db_item(
        "sessions",
        "session_id",
        session_id,
        "last_activity",
        datetime.datetime.now().isoformat(),
    )
