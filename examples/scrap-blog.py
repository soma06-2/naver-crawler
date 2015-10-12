# -*- coding: utf-8 -*-
# import scrapy
import sys
sys.path.insert(0, '../')

from crawler import NaverCrawler

crawler = NaverCrawler()

results = crawler.find_blog_posts(u'피플 킬링 피플 다잉')

print "Total Reviews: %d" % (len(results))
print ""

for review in results:
    print '#'*50
    print review['content']
    print ""
