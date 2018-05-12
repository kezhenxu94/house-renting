# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
from scrapy.exporters import BaseItemExporter


class ESItemExporter(BaseItemExporter):
    client = Elasticsearch(hosts='127.0.0.1')
    index = 'house_renting'
    doc_type = 'Post'

    def start_exporting(self):
        pass

    def finish_exporting(self):
        pass

    def export_item(self, item):
        self.client.index(index=self.index, doc_type=self.doc_type, body=dict(item))
        return item
