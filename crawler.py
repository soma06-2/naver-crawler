# -*- coding: utf-8 -*-
# import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class NaverCrawler():
    def find_blog_posts(self, search):
        results = []

        proc = CrawlerProcess(get_project_settings())

        proc.crawl('naver-blog', results, search)
        proc.start()

        return results

    def find_product_reviews(self, productId):
        results = []

        proc = CrawlerProcess(get_project_settings())

        proc.crawl('naver-shopping', results, productId)
        proc.start()

        return results
