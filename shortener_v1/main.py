"""
PYTHONPATH=$(pwd):$PYTHONPATH python -m cProfile -o program.prof shortener_v1/main.py
"""
import sqlite3

from shortener_v1 import shortkey, db


def main(cursor):
    url = 'https://avatars.mds.yandex.net/get-pdb/879561/6d756018-671f-4cb4-b5a4-f4a0a681348f/s1200'

    return shortkey.short(cursor, url)


if __name__ == '__main__':
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute(db.create_sql)

    for _ in range(1000):
        main(cursor)
