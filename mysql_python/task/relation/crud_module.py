from connection_module import *


@execute
def save(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)


@execute
def save_many(cursor: Cursor, query: str, params: tuple):
    cursor.executemany(query, params)


@execute
def find_all(cursor: Cursor, query: str) -> list:
    cursor.execute(query)
    return cursor.fetchall()


@execute
def find_all_by(cursor: Cursor, query: str, params: tuple) -> list:
    cursor.execute(query, params)
    return cursor.fetchall()

@execute
def find_by_id(cursor: Cursor, query: str, params: tuple) -> dict:
    cursor.execute(query, params)
    return cursor.fetchone()


@execute
def update(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)


@execute
def delete(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)
