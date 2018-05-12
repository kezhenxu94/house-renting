# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from house_renting.exporters import ESItemExporter


class HouseRentingPipeline(object):
    def process_item(self, item, spider):
        return item


class ESPipeline(object):
    exporter = None

    def open_spider(self, spider):
        self.exporter = ESItemExporter()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
