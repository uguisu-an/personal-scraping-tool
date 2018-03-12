import os
import json as js


JSON_FILE = './cache/pokemon_abilities.json'


def data_is_cached():
    return os.path.exists(JSON_FILE)


def crawl():
    res = os.system('scrapy crawl pokemon_abilities -o {}'.format(JSON_FILE))
    if res != 0:
        raise RuntimeError('Crawling is Failure.')


def load_items():
    st = open(JSON_FILE)
    json = js.load(st)
    return json[0]['abilities']


def print_abilities():
    abilities = load_items()
    for ability in abilities:
        print(ability.strip())


if __name__ == '__main__':
    if not data_is_cached():
        crawl()
    print_abilities()
