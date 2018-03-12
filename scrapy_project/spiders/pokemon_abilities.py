# -*- coding: utf-8 -*-
import scrapy


class PokemonAbilitySpider(scrapy.Spider):
    name = 'pokemon_abilities'
    allowed_domains = ['bulbapedia.bulbagarden.net']
    start_urls = ['http://bulbapedia.bulbagarden.net/wiki/Ability']

    def parse(self, response):
        abilities = response.xpath('//*[@id="mw-content-text"]/table[3]/tr/td/table/tr[position()>0]/td[2]/a/text()')
        yield {
            'abilities': abilities.extract(),
        }
