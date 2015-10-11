import scrapy
from naver_crawler.items import Review
import re
import math
from urlparse import urlparse
from urlparse import parse_qs

class BlogSpider(scrapy.Spider):
    name = "naver-blog"
    # allowed_domains = ["cafeblog.search.naver.com", "blog.naver.com"]
    # start_urls = [getPageURL(1)]

    def __init__(self, search):
        self.search = search.replace(' ', '+')

        self.start_urls = ["http://cafeblog.search.naver.com/search.naver?sm=mtb_pcv&where=post&ie=utf8&query=%s" % (self.search)]

    def parse(self, response):
        for url in response.css("#main_pack > div.paging > a::attr('href')").extract():
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parseSearch)

    def parseSearch(self, response):
        for url in response.css(".sh_blog_top > dl > dt > a::attr('href')").extract():
            if not "http://blog." in url:
                continue

            uri = urlparse(url)

            try:
                yield scrapy.Request(("%s/%s" % (url.split('?')[0], parse_qs(uri.query)['logNo'][0])).replace('http://blog.', 'http://m.blog.'), callback=self.parsePost)
            except:
                pass

        for url in response.css("#main_pack > div.paging > a::attr('href')").extract():
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parseSearch)

    def parsePost(self, response):
        review = Review()

        review['content'] = (''.join(response.xpath('//*[@id="viewTypeSelector"]/p/text()').extract())).strip()

        if len(review['content']) != 0:
            yield review
