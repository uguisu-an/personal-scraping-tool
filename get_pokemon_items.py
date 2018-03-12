import os
import json as js


JSON_FILE = './cache/pokemon_items.json'


def data_is_cached():
    return os.path.exists(JSON_FILE)


def crawl():
    res = os.system('scrapy crawl pokemon_items -o {}'.format(JSON_FILE))
    if res != 0:
        raise RuntimeError('Crawling is Failure.')


def load_items():
    st = open(JSON_FILE)
    json = js.load(st)
    return json[0]['items']


def print_items():
    items = load_items()
    for item in items:
        print(item.strip())


if __name__ == '__main__':
    if not data_is_cached():
        crawl()
    print_items()
