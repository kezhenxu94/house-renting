# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from redis import Redis
from scrapy.conf import settings
from scrapy.downloadermiddlewares.retry import RetryMiddleware

from house_renting import proxies


class HouseRentingAgentMiddleware(object):
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.user_agents))


class HouseRentingRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        super(HouseRentingRetryMiddleware, self).__init__(settings)
        self.proxies = proxies.proxies

    def process_exception(self, request, exception, spider):
        if len(self.proxies) > 0:
            request.meta['proxy'] = random.choice(self.proxies)
        return super(HouseRentingRetryMiddleware, self).process_exception(request, exception, spider)


class HouseRentingProxyMiddleware(object):
    def __init__(self):
        redis_host = settings.get('REDIS_HOST')
        redis_port = settings.get('REDIS_PORT', default=6379)

        if redis_host is not None:
            self.r_client = Redis(host=redis_host, port=redis_port)

        self.proxies = proxies.proxies

    def process_request(self, request, spider):
        if len(self.proxies) > 0:
            request.meta['proxy'] = random.choice(self.proxies)
