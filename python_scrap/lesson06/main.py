"""Задание:
1) Взять любую категорию объявлений на сайте юла (например недвижимость или авто).
И собрать с использованием ItemLoader следующие данные:
- Название
- Все фото
- Параметры товара в объявлении
2) С использованием output_processor и input_processor реализовать очистку и преобразование данных.
Значения цен должны быть в виде числового значения.
3*) Написать универсальный обработчик параметров объявлений, который будет формировать данные вне зависимости от их типа
и количества.
4*) Реализовать более удобную струткуру для хранения скачиваемых фотографий
5) Дополнительно: Перевести всех пауков сбора данных о вакансиях на ItemLoader и привести к единой структуре.
"""
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from goodsparser import settings
from goodsparser.spiders.youla import YoulaSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(YoulaSpider, sections=['kompyutery'])
    process.start()
