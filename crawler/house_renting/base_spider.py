# -*- coding: utf-8 -*-
from __future__ import print_function
from scrapy.spiders import CrawlSpider


class BaseCrawlSpider(CrawlSpider):
    def start_requests(self):
        cities = self.settings.get('cities', [])
        city_url_mappings = self.settings.get('available_cities_map', {})

        for city in cities:
            city_url = city_url_mappings[city]
            if city_url is None:
                print('Cannot crawl house renting data from city: ', city)
            else:
                yield self.make_requests_from_url(city_url)
