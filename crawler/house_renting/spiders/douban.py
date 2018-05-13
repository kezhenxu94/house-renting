# -*- coding: utf-8 -*-

from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import Rule, CrawlSpider

from house_renting.items import HouseRentingDoubanItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/group/tianhezufang/discussion?start=0']

    rules = (
        Rule(LinkExtractor(allow=r'/group/tianhezufang/discussion\?start=\d+$',
                           restrict_css=('div#content div.article table', 'div#content div.article div.paginator')),
             follow=True),
        Rule(LinkExtractor(allow=r'/group/topic/\d+/$'), callback='parse_item'),
    )

    def parse_item(self, response):
        selector = Selector(response=response)
        selector.css('div#content div.article div.topic-content')

        item_loader = ItemLoader(item=HouseRentingDoubanItem(), selector=selector, response=response)
        item_loader.add_css(field_name='title', css='table.infobox *::text')
        item_loader.add_css(field_name='title', css='div#content > h1:first-child::text')
        item_loader.add_value(field_name='source', value=self.name)
        item_loader.add_css(field_name='author', css='h3 span.from a::text')
        item_loader.add_css(field_name='image_urls', css='div.topic-content div#link-report img::attr(src)')
        item_loader.add_css(field_name='author_link', css='h3 span.from a::attr(href)')
        item_loader.add_css(field_name='content', css='div.topic-content div#link-report *::text', re=r'\s*(.*)\s*')
        item_loader.add_value(field_name='source_url', value=response.url)
        item_loader.add_css(field_name='publish_time', css='h3 span:last-child::text',
                            re=r'\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*')

        yield item_loader.load_item()
