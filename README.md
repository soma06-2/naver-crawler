# Naver Crawler

scraps blog posts and product reviews of naver.

## Requirements

### Scrapy

```sh
$ sudo pip install scrapy
```

#### when troubles come from other libraries

there can be occured errors with OS X. perhaps, you need googling to solve them.

if you

* can't find image: execute this command in terminal: `export DYLD_LIBRARY_PATH=$HOME/anaconda/lib`
* can't import xmlrpc_clinet: read [this stack overflow answers](http://stackoverflow.com/questions/30964836/scrapy-throws-importerror-cannot-import-name-xmlrpc-client)

## Installation

```sh
$ git clone git@github.com:soma06-2/naver-crawler.git
```

prepend belew code to your python script to use crawler

```py
from naver_crawler.crawler import NaverCrawler
```

## Configuration

If you need more options such as download delay, max depth, domain restrict and timeout, etc, then see [Scrapy Configuration](http://doc.scrapy.org/en/master/topics/settings.html).

## Usage

Below functions are provided as terminal command. `{$variable:type}` format should be converted to normal text. Like this:

* {$a:int}: 111
* {$b:string}: fefwfe11021fwe
* {$c:string,JSON}: [{"JSON":"type"}]

### API: Crawling product reviews

#### in Python Script

```py
crawler = NaverCrawler()

results = crawler.find_product_reviews(7789434971)

print "Total Reviews: %d" % (len(results))
print ""

for review in results:
    print '#'*50
    print review['content']
    print ""
```

#### Through Terminal

```sh
$ scrapy crawl naver-shopping -a entityId={$productId:int} -o {$filename:string}
```

##### Parameters

* $productId: naver product id
* $filename: destination of result file

##### Result

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

#### in Python Script

```py
crawler = NaverCrawler()

results = crawler.find_blog_posts(u'피플 킬링 피플 다잉')

print "Total Reviews: %d" % (len(results))
print ""

for review in results:
    print '#'*50
    print review['content']
    print ""
```

#### Through Terminal

```sh
$ scrapy crawl naver-blog -a search="{$keyword:string}" -o {$filename:string}
```

*care above `$keyword` should be in quotes if `$keyword` contains spaces.*

##### Parameters

* $keyword: word to search in naver blog posts
* $filename: destination of result file

##### Result

```js
[{"content": "Post 1"},
{"content": "Post 2"},
{"content": "Post 3"},
....
....
....
{"content": "Post n"}]
```