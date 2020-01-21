# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader.processors import Identity, MapCompose, TakeFirst


def strip_text(value: str):
    if value:
        return value.replace(' ', '').strip()
    else:
        return None


def int_value(value: str):
    if value:
        try:
            return int(strip_text(value))
        except ValueError as e:
            print(e, 'for:', value)
            return None
    else:
        return None


class DictCollector(object):

    def __call__(self, values):
        if values:
            return dict(zip(values[::2], values[1::2]))
        else:
            return None


class GoodsParserItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field(
        output_processor=Identity()
    )
    name = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(int_value),
        output_processor=TakeFirst(),
    )
    currency = scrapy.Field(
        input_processor=MapCompose(strip_text),
        output_processor=TakeFirst(),
    )
    images = scrapy.Field(
        output_processor=Identity()
    )
    description = scrapy.Field(
        input_processor=DictCollector()
    )
    attributes = scrapy.Field(
        input_processor=DictCollector()
    )
