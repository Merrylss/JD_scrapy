# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy import Request
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
# from bs4 import BeautifulSoup
from ..items import JingdongItem


class PhoneSpider(RedisCrawlSpider):
    name = 'phone'
    # allowed_domains = ['passport.jd.com']
    # start_urls = ['https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fshouji.jd.com%2F']

    redis_key = 'phone:start_url'
    # 页码的匹配规则
    pageLink = LinkExtractor(allow='&page=')

    rules = [
        Rule(pageLink, callback='parse_item', follow=True),
    ]

    def parse_item(self, response):
        linkNode = response.xpath('//*[@id="plist"]/ul/li')
        for node in linkNode:
            url = node.xpath('./div/div[1]/a/@href')[0].extract()
            # print('=============', "http:"+url)
            realUrl = "http:"+url
            # print("-----------------------------", realUrl)
            yield Request(realUrl, callback=self.phone_info)

    def phone_info(self, response):
        print('-------------------------', response.url)
        # item = JingdongItem()
        # item['name'] = response.xpath('')


