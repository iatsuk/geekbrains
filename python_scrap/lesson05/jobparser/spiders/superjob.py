# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

from jobparser.items import JobparserItem


class SuperJobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.f-test-link-Dalshe::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancies = response.css('div.f-test-vacancy-item div._3syPg a._1QIBo::attr(href)').extract()
        for vacancy in vacancies:
            yield response.follow(vacancy, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        # host
        host = response.css('meta[property="og:site_name"]::attr(content)').extract_first().lower()
        # url
        url = response.css('meta[property="og:url"]::attr(content)').extract_first()
        # description
        description = response.css('meta[property="og:description"]::attr(content)').extract_first()
        title, salary = description.split(', ')
        # name
        name = title[len('Вакансия '):title.rfind(' в компании ')]
        # company
        company = title[title.rfind(' в компании ') + len(' в компании '):].strip()
        # salary
        salary = salary[len('зарплата '):-1]
        if salary == 'по договорённости':
            salary_min, salary_max, salary_currency = None, None, None
        else:
            salary_currency_index = next(i for i, j in list(enumerate(salary, 1))[::-1] if j.isdigit())
            salary_currency = salary[salary_currency_index + 1:]
            salary = salary[:salary_currency_index].replace(' ', '')
            if '-' in salary:
                salary_min, salary_max = salary.split('-')
            else:
                salary_min = salary_max = salary
                text_range = response.css('span._2Wp8I.ZON4b *::text').extract_first().lower()
                if text_range.startswith('до'):
                    salary_min = None
                else:  # от
                    salary_max = None
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
