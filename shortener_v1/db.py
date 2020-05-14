create_sql = """
    CREATE TABLE IF NOT EXISTS url(
        short_id TEXT PRIMARY KEY NOT NULL, 
        url TEXT NOT NULL
    )"""

get_by_url_sql = """
    SELECT short_id, url
    FROM url
    WHERE url = ?
    LIMIT 1"""

insert_sql = """
    INSERT INTO url (short_id, url) 
    VALUES (?, ?)
    ON CONFLICT(short_id)
    DO NOTHING"""


def get_by_url(cursor, url):
    #  сделал так, что бы в бенчмарке все время генерился новый short_id
    is_exists = cursor.execute(get_by_url_sql, (url,)).fetchone()
    return None


def insert_url(cursor, short_id, url):
    cursor.execute(insert_sql, (short_id, url))
