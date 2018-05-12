from scrapy.commands.crawl import Command
from scrapy.exceptions import UsageError


class CustomCrawlCommand(Command):
    def run(self, args, opts):
        if len(args) < 1:
            raise UsageError()
        elif len(args) > 1:
            raise UsageError("running 'scrapy crawl' with more than one spider is no longer supported")
        spider_name = args[0]

        spider_settings_path = self.settings.getdict('SPIDER_SETTINGS', {}).get(spider_name, None)
        if spider_settings_path is not None:
            self.settings.setmodule(spider_settings_path, priority='cmdline')

        self.crawler_process.crawl(spider_name, **opts.spargs)
        self.crawler_process.start()
