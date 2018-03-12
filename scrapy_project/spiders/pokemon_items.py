# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'pokemon_items'
    allowed_domains = ['bulbapedia.bulbagarden.net']
    start_urls = ['https://bulbapedia.bulbagarden.net/wiki/List_of_items_by_name']

    def parse(self, response):
        content = response.css('#mw-content-text')
        items = content.css('.roundy tr:nth-child(n+1) td:nth-child(2) a::text')
        yield {
            'items': items.extract(),
        }
