# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy import Spider
from scrapy.selector import Selector


class CrawlerItem(scrapy.Item):
    User = scrapy.Field()
    Comment = scrapy.Field()
    Time = scrapy.Field()


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd/samsung-galaxy-a50",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//ul[@class="listcomment"]/li')

        for question in questions:
            item = CrawlerItem()

            item['User'] = question.xpath(
                'div[@class="rowuser"]/a/strong/text()').extract_first()
            item['Comment'] = question.xpath(
                'div[@class="question"]/text()').extract_first()
            item['Time'] = question.xpath(
                'div[@class="actionuser"]/a[@class="time"]/text()').extract_first()

            yield item