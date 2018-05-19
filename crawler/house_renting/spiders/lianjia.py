# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from house_renting.items import HouseRentingLianjiaItem


class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']

    rules = (
        Rule(LinkExtractor(allow=r'/zufang/(pg\d+/)?$', restrict_css=('div.list-wrap > ul > li', 'div.page-box')),
             follow=True),
        Rule(LinkExtractor(allow=r'/zufang/\w+.html$'), callback='parse_item'),
    )

    def start_requests(self):
        cities = self.settings.get('cities', [])
        city_url_mappings = self.settings.get('available_cities_map', {})

        print 'cities:', cities, 'city_url_mappings:', city_url_mappings

        for city in cities:
            if city_url_mappings[city] is None:
                print 'Cannot crawl house renting data from city: ', city
            else:
                yield self.make_requests_from_url(city_url_mappings[city])

    def parse_item(self, response):
        item_loader = ItemLoader(item=HouseRentingLianjiaItem(), response=response)

        item_loader.add_css(field_name='title', css='div.title *::text')
        item_loader.add_value(field_name='source', value=self.name)
        item_loader.add_css(field_name='author', css='div.brokerName > a.name::text')
        item_loader.add_css(field_name='image_urls', css='div.thumbnail > ul > li > img::attr(src)')
        item_loader.add_css(field_name='author_link', css='div.brokerName > a.name::attr(href)')
        item_loader.add_css(field_name='content', css='div.introduction *::text', re=r'\s*(.*)\s*')
        item_loader.add_value(field_name='source_url', value=response.url)
        item_loader.add_css(field_name='publish_time', css='div.zf-room > p::text')

        item_loader.add_css(field_name='price', css='div.price > span.total::text')
        item_loader.add_css(field_name='detail', css='div.zf-room *::text')

        yield item_loader.load_item()
