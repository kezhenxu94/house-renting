# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider


class BaseCrawlSpider(CrawlSpider):
    def start_requests(self):
        cities = self.settings.get('cities', [])
        city_url_mappings = self.settings.get('available_cities_map', {})

        print 'cities:', cities, 'city_url_mappings:', city_url_mappings

        for city in cities:
            if city_url_mappings[city] is None:
                print 'Cannot crawl house renting data from city: ', city
            else:
                yield self.make_requests_from_url(city_url_mappings[city])
