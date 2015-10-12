# -*- coding: utf-8 -*-
# import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import sys
sys.path.insert(0, '../')

from naver_crawler.spiders.blog import BlogSpider

results = []

proc = CrawlerProcess(get_project_settings())

proc.crawl('naver-shopping', results, '7789434971')
proc.start()

print "Total Reviews: %d" % (len(results))
print ""

for review in results:
    print '#'*50
    print review['content']
    print ""
