# Naver Crawler

scraps blog posts and product reviews of naver.

## Requirements

### Scrapy

`sudo pip install scrapy`

#### when troubles come from other libraries

there can be occured errors with OS X. perhaps, you need googling to solve them.

if you

* can't find image: execute this command in terminal: `export DYLD_LIBRARY_PATH=$HOME/anaconda/lib`
* can't import xmlrpc_clinet: read [this stack overflow answers](http://stackoverflow.com/questions/30964836/scrapy-throws-importerror-cannot-import-name-xmlrpc-client)

## Installation

```sh
git clone git@github.com:soma06-2/naver-crawler.git
cd ./naver-crawler
```

## Examples

Below explains how to use naver-crawler in python script. If you need more options, see [Scrapy Configuration](http://doc.scrapy.org/en/master/topics/settings.html).

### Crawling Naver Product
```py
# -*- coding: utf-8 -*-
# import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
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
```

### Crawling Naver Blog Posts
```py
# -*- coding: utf-8 -*-
# import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
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
```

## Usage

Below functions are provided as terminal command. `{$variable:type}` format should be converted to normal text. Like this:

* {$a:int}: 111
* {$b:string}: fefwfe11021fwe
* {$c:string,JSON}: [{"JSON":"type"}]

### API: Crawling product reviews

```sh
scrapy crawl naver-shopping -a entityId={$productId:int} -o {$filename:string}
```

#### Parameters

* $productId: naver product id
* $filename: destination of result file

#### Result

```js
[{"content": "Review 1"},
{"content": "Review 2"},
{"content": "Review 3"},
....
....
....
{"content": "Review n"}]
```

### API: Crawling blog posts

```
scrapy crawl naver-blog -a search="{$keyword:string}" -o {$filename:string}
```

*care above `$keyword` should be in quotes if `$keyword` contains spaces.*

#### Parameters

* $keyword: word to search in naver blog posts
* $filename: destination of result file

#### Result

```js
[{"content": "Post 1"},
{"content": "Post 2"},
{"content": "Post 3"},
....
....
....
{"content": "Post n"}]
```