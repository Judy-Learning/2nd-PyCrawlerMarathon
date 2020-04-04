# -*- coding: utf-8 -*-
import scrapy


class Day026HwSpider(scrapy.Spider):
    name = 'Day026_HW'
    allowed_domains = ['https://www.ptt.cc/bbs/index.html']
    start_urls = ['http://https://www.ptt.cc/bbs/index.html/']

    def parse(self, response):
        print(response.text)
        pass
