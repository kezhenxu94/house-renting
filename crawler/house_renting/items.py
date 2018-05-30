# -*- coding: utf-8 -*-

import datetime
import re
import time

import scrapy
from scrapy.loader.processors import Join, MapCompose, Compose, TakeFirst


def filter_title(value):
    return value.strip() if value != u'标题：' else None


def filter_content(value):
    return value if len(value) > 0 else None


class HouseRentingBaseItem(scrapy.Item):
    item_id = scrapy.Field()
    title = scrapy.Field(input_processor=MapCompose(str.strip, filter_title),
                         output_processor=Compose(TakeFirst(), str.strip))
    source = scrapy.Field(output_processor=Join())
    author = scrapy.Field(input_processor=MapCompose(str.strip),
                          output_processor=Compose(Join(), str.strip))
    image_urls = scrapy.Field()
    images = scrapy.Field()
    author_link = scrapy.Field(output_processor=Join())
    content = scrapy.Field(input_processor=MapCompose(str.strip, filter_content),
                           output_processor=Compose(Join(separator=u'\n')))
    source_url = scrapy.Field(output_processor=Join())
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip))


def publish_time_serializer_douban(value):
    return int(time.mktime(datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S").timetuple()))


class HouseRentingDoubanItem(HouseRentingBaseItem):
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip, publish_time_serializer_douban))


def publish_time_serializer(value):
    minutes_ago = re.compile(u'.*?(\d+)分钟前.*').search(value)
    hours_ago = re.compile(u'.*?(\d+)小时前.*').search(value)
    days_ago = re.compile(u'.*?(\d+)天前.*').search(value)
    date = re.compile(u'.*?(\d+)-(\d+).*').search(value)

    if minutes_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(minutes=int(minutes_ago.group(1)))
    elif hours_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(hours=int(hours_ago.group(1)))
    elif days_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(days=int(days_ago.group(1)))
    else:
        publish_time = datetime.datetime.today().replace(month=int(date.group(1)), day=int(date.group(2)))

    if publish_time is not None:
        return int(time.mktime(publish_time.timetuple()))


def price_serializer_58(value):
    price = re.compile(u'\s*(\d+)\s*元/月.*').search(value)
    if price:
        return int(price.group(1))
    return None


class HouseRenting58Item(HouseRentingBaseItem):
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip, publish_time_serializer))
    price = scrapy.Field(input_processor=MapCompose(str.strip),
                         output_processor=Compose(Join(), str.strip, price_serializer_58))
    detail = scrapy.Field(input_processor=MapCompose(str.strip),
                          output_processor=Compose(Join(), str.strip))


class HouseRentingLianjiaItem(HouseRentingBaseItem):
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip, publish_time_serializer))
    price = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=Compose(Join(), str.strip))
    detail = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=Compose(Join(), str.strip))
