# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

import redis
from scrapy.conf import settings
from scrapy.exceptions import DropItem

from house_renting.exporters import ESItemExporter


class HouseRentingPipeline(object):
    def process_item(self, item, spider):
        m = hashlib.md5()
        m.update(item['source_url'].encode('utf-8'))
        item['item_id'] = m.hexdigest()
        return item


class ESPipeline(object):
    exporter = None

    def open_spider(self, spider):
        self.exporter = ESItemExporter()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class DuplicatesPipeline(object):
    def __init__(self):
        redis_host = settings.get('REDIS_HOST')
        redis_port = settings.get('REDIS_PORT', default=6379)

        if redis_host is not None:
            self.r_client = redis.Redis(host=redis_host, port=redis_port)

    def process_item(self, item, spider):
        if self.r_client is None:
            return item

        if 'item_id' in item:
            item_id = item['item_id']
            existed_id = self.r_client.get(item_id)
            if existed_id is not None:
                raise DropItem("Duplicate item found: %s" % item)
            self.r_client.set(item_id, 'SEEN')

        return item
