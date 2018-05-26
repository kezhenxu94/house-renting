# -*- coding: utf-8 -*-
import json

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import Rule

from house_renting.base_spider import BaseCrawlSpider
from house_renting.items import HouseRentingLianjiaItem

current_page = 0


class LianjiaSpider(BaseCrawlSpider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']

    rules = (
        Rule(LinkExtractor(allow=r'/zufang/(pg\d+/)?$', restrict_css='div.list-wrap > ul > li'), follow=True),
        Rule(LinkExtractor(allow=r'/zufang/\w+.html$'), callback='parse_item'),
    )

    def parse_start_url(self, response):
        page_data = response.css('div.page-box::attr(page-data)').extract_first()
        if page_data is None:
            return

        page_data = json.loads(page_data)
        total_page = page_data['totalPage']
        if total_page is None:
            return

        page_url_pattern = response.css('div.page-box::attr(page-url)').extract_first()
        if page_url_pattern is None:
            return

        for page in range(0, total_page):
            yield response.follow(page_url_pattern.replace('{page}', str(page)))

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
