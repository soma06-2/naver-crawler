# -*- coding: utf-8 -*-
# import scrapy
import sys
sys.path.insert(0, '../')

from crawler import NaverCrawler

crawler = NaverCrawler()

results = crawler.find_product_reviews(7789434971)

print "Total Reviews: %d" % (len(results))
print ""

for review in results:
    print '#'*50
    print review['content']
    print ""
