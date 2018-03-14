import scrapy
import re


class PokemonMovesSpider(scrapy.Spider):
    name = 'moves'
    allow_domain = ['bulbapedia.bulbagarden.net']
    start_urls = ['https://bulbapedia.bulbagarden.net/wiki/List_of_moves']

    def parse(self, response):
        table = response.css('#mw-content-text > table:nth-child(4) > tr > td > table')
        for row in table.css('tr')[1:]:
            yield {
                'id': text_to_int(row.css('td:nth-child(1)::text').extract_first()),
                'name': row.css('td:nth-child(2) a::text').extract_first().strip(),
                'type': row.css('td:nth-child(3) a span::text').extract_first().strip(),
                'category': row.css('td:nth-child(4) a span::text').extract_first().strip(),
                'pp': text_to_int(row.css('td:nth-child(6)::text').extract_first()),
                'power': text_to_int(row.css('td:nth-child(7)::text').extract_first().strip()),
                'accuracy': text_to_int(row.css('td:nth-child(8)::text').extract_first()),
            }


def text_to_int(text):
    pattern = '[^0-9]+'
    if re.findall(pattern, text):
        text = re.sub(pattern, '', text)
    if not text:
        return 0
    return int(text)
