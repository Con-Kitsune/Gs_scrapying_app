# -*- coding: utf-8 -*-
import scrapy

from scrapying_app.items import ScrapyingAppItem

class SoccerkingSpider(scrapy.Spider):
    name = 'soccerking'
    allowed_domains = ['soccer-king.jp']
    start_urls = ['http://soccer-king.jp/日本代表']

    def parse(self, response):

        for url in response.css('div.japanSpecial  a.japanTopic::attr("href")').extract():
            # item = ScrapyingAppItem()
            # item['url'] = response.css('div.japanSpecial  a.japanTopic::attr("href")').extract()
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
            item = ScrapyingAppItem()
            item['headline'] = response.css('div.contents-main__inner h1::text').extract()
            item['thumbnail'] = response.css('div.mainVisual__inner img::attr("src")').extract()
            item['url'] = response.url
            # css('div.japanSpecial  a.japanTopic::attr("href")').extract()
            yield item
        # print(response.css('ul.list-2col__list a::attr("href")').extract())
