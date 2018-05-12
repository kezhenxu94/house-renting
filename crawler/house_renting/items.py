# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import datetime
import time

import scrapy
from scrapy.loader.processors import Join, MapCompose, Compose, TakeFirst


def filter_title(value):
    return value if value != u'标题：' else None


def publish_time_serializer(value):
    return int(time.mktime(datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S").timetuple()))


class HouseRentingItem(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(unicode.strip, filter_title),
                         output_processor=Compose(TakeFirst(), unicode.strip))
    source = scrapy.Field(output_processor=Join())
    author = scrapy.Field(input_processor=MapCompose(unicode.strip),
                          output_processor=Compose(Join(), unicode.strip))
    image_urls = scrapy.Field()
    images = scrapy.Field()
    author_link = scrapy.Field(output_processor=Join())
    content = scrapy.Field(input_processor=MapCompose(unicode.strip),
                           output_processor=Compose(Join(separator=u'\n'), unicode.strip))
    source_url = scrapy.Field(output_processor=Join())
    publish_time = scrapy.Field(input_processor=MapCompose(unicode.strip),
                                output_processor=Compose(Join(), unicode.strip, publish_time_serializer))
