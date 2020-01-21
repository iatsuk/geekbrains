# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

from goodsparser.items import GoodsParserItem


class YoulaSpider(scrapy.Spider):
    name = 'youla'
    allowed_domains = ['youla.ru']

    def __init__(self, sections: list):
        start_urls = [f'https://youla.ru/moskva/{section}' for section in sections]
        super().__init__(start_urls=start_urls)

    def parse(self, response: HtmlResponse):
        # next_page = response.css('div.pagination__button > a._paginator_next_button::attr(href)').extract_first()
        # yield response.follow(next_page, callback=self.parse)

        items = response.css('ul.product_list > li.product_item > a::attr(href)').extract()
        for item in items:
            yield response.follow(item, callback=self.item_parse)

    def item_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=GoodsParserItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_css('name', 'h2.sc-fjdhpX *::text')
        loader.add_css('price', 'span[data-test-component="Price"]::text')
        loader.add_css('currency', 'span[data-test-component="Price"] > span > i::text')
        loader.add_css('images', 'div[data-test-component="ProductGallery"] > div.kYGXDl img::attr(src)')
        loader.add_css('description', 'li[data-test-block="Description"] > dl > *::text')
        loader.add_css('attributes', 'li[data-test-block="Attributes"] > dl > *::text')
        yield loader.load_item()
