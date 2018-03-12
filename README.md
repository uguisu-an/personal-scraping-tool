# スクレイピングツール

## 概要

英語版のポケモンWikiから能力と道具のリストを取ってくるやつ

## 必要な環境

* Python 3.6.4
* Scrapy 1.5.0

## 使用例

```bash
$ python get_pokemon_items.py | sed -e 's/[^0-9a-zA-Z]\{1,\}//g'
$ python get_pokemon_abilities.py | sed -e 's/[^0-9a-zA-Z]\{1,\}//g'
```
