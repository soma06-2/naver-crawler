import scrapy
from naver_crawler.items import Review
import re
import math


class ShoppingSpider(scrapy.Spider):
    name = "naver-shopping"
    # allowed_domains = ["sho.org"]
    # start_urls = [getPageURL(1)]

    def __init__(self, entityId):
        self.entityId = entityId

        self.start_urls = [
            "http://shopping.naver.com/detail/detail.nhn?nv_mid=%s" % (self.entityId)]

    def getURL(self, page):
        return "http://shopping.naver.com/detail/section_user_review.nhn?nv_mid=%s&page=%s" % (self.entityId, page)

    def parse(self, response):
        max_pages = int(math.ceil(int(response.xpath(
            '//*[@id="review_user"]/em/text()').extract()[0].replace(',', '')) / 20))

        for i in xrange(1, max_pages + 2):
            yield scrapy.Request(self.getURL(i), callback=self.bringContent)

    def bringContent(self, response):
        for row in response.xpath('//*[@id="lst_review"]/li'):
            review = Review()

            review['content'] = ''.join(row.css('.atc::text').extract()).strip()

            if len(review['content']) == 0:
                continue

            yield review
