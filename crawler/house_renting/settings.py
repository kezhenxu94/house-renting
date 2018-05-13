# -*- coding: utf-8 -*-

BOT_NAME = 'house_renting'

COMMANDS_MODULE = 'house_renting.commands'
SPIDER_MODULES = ['house_renting.spiders']
NEWSPIDER_MODULE = 'house_renting.spiders'

USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) ' \
             'AppleWebKit/602.1.38 (KHTML, like Gecko) ' \
             'Version/10.0 Mobile/14A300 Safari/602.1'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 10

CONCURRENT_REQUESTS_PER_DOMAIN = 1

COOKIES_ENABLED = True

TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# SPIDER_MIDDLEWARES = {
#    'house_renting.middlewares.HouseRentingSpiderMiddleware': 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#    'house_renting.middlewares.MyCustomDownloaderMiddleware': 543,
# }

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 100,
    'house_renting.pipelines.ESPipeline': 300,
}
IMAGES_STORE = '/tmp/house_renting'
MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_LEVEL = 'DEBUG'
