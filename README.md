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
git clone # fill repository address
cd ./naver-crawler/naver_crawler # second is 'underscore'!
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

* $productId: naver product id
* $filename: destination of result file

### API: Crawling blog posts

```
scrapy crawl naver-blog -a search="{$keyword:string}" -o {$filename:string}
```

*care above $keyword should be in quotes if $keyword contains spaces*

* $keyword: word to search in naver blog posts
* $filename: destination of result file