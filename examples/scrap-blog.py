# -*- coding: utf-8 -*-
# import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import sys
sys.path.insert(0, '../')

from naver_crawler.spiders.blog import BlogSpider

results = []

proc = CrawlerProcess(get_project_settings())

proc.crawl('naver-blog', results, u'피플 킬링 피플 다잉')
proc.start()

print "Total Reviews: %d" % (len(results))
print ""

for review in results:
    print '#'*50
    print review['content']
    print ""
