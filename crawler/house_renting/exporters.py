# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from scrapy.conf import settings
from scrapy.exporters import BaseItemExporter


class ESItemExporter(BaseItemExporter):
    index = 'house_renting'
    doc_type = 'Post'

    def __init__(self, **kwargs):
        super(ESItemExporter, self).__init__(**kwargs)

        self.elastic_hosts = settings.get('ELASTIC_HOSTS')

        if self.elastic_hosts is not None:
            self.client = Elasticsearch(hosts=self.elastic_hosts)

    def start_exporting(self):
        pass

    def finish_exporting(self):
        pass

    def export_item(self, item):
        if self.client is None:
            return item

        item_id = item['item_id']
        self.client.index(index=self.index, doc_type=self.doc_type, body=dict(item), id=item_id)
        return item
