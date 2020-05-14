from shortid import ShortId

from .db import get_by_url, insert_url


_sid = ShortId()


def generate() -> str:
    return _sid.generate()


def short(cursor, url):
    short_url = get_by_url(cursor, url)
    if short_url:
        short_id = short_url[0]
    else:
        short_id = generate()
        insert_url(cursor, short_id, url)

    return short_id
