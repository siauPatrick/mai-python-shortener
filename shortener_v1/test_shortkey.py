"""
python -m pytest shortener_v1 --benchmark-autosave
"""
import sqlite3

from shortener_v1 import shortkey, db


def test_short_url_shortid(benchmark):
    url = 'https://www.avito.ru/moskva/sobaki/velsh_korgi_pembrok_schenki_1626593770'
    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    cursor.execute(db.create_sql)

    benchmark.pedantic(shortkey.short, args=(cursor, url), iterations=10_000, rounds=100, warmup_rounds=30)
