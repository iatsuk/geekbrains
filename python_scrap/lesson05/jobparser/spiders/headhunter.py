# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from urllib.parse import urljoin, urlparse
import tldextract

from jobparser.items import JobparserItem


class HeadHunterSpider(scrapy.Spider):
    name = 'headhunter'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancies = response.css('div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)').extract()
        for vacancy in vacancies:
            yield response.follow(vacancy, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        # host without subdomains
        parsed_uri = tldextract.extract(response.url)
        host = "{domain}.{suffix}".format(domain=parsed_uri.domain, suffix=parsed_uri.suffix).lower()
        # url
        url = urljoin(response.url, urlparse(response.url).path)
        # name
        name = response.css('h1.header *::text').extract_first()
        # company
        company = response.css('*.vacancy-company-name-wrapper > span[itemprop="identifier"] > meta[itemprop="name"]::attr(content)').extract_first().strip()
        # salary
        salary_data = response.css('div.vacancy-title > span[itemprop="baseSalary"]')
        salary_min = salary_data.css('meta[itemprop="minValue"]::attr(content)').extract_first()
        salary_max = salary_data.css('meta[itemprop="maxValue"]::attr(content)').extract_first()
        salary_currency = salary_data.css('meta[itemprop="currency"]::attr(content)').extract_first()
        # return result
        yield JobparserItem(
            host=host,
            url=url,
            name=name,
            company=company,
            salary_min=salary_min,
            salary_max=salary_max,
            salary_currency=salary_currency,
        )
