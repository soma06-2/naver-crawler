# Naver Crawler

scraps blog posts and product reviews of naver.

## Requirements

### Scrapy

`sudo pip install scrapy`

#### when troubles come from other libraries

there can be occured errors with OS X. perhaps, you need googling to solve them.

When can't find image: `export DYLD_LIBRARY_PATH=$HOME/anaconda/lib`

## Installation

```sh
git clone # fill repository address
cd ./naver-crawler/naver_crawler # second is 'underscore'!
```

## Usage

Below functions are provided as terminal command

### API: Crawling product reviews

`scrapy crawl naver-shopping -a entityId={$productId:int} -o {$filename:string}`

* $productId: naver product id
* $filename: destination of result file

### API: Crawling blog posts

`scrapy crawl naver-blog -a search="{$keyword:string}" -o {$filename:string}`
*care $keyword should be in quotes if $keyword contains spaces*

* $keyword: word to search
* $filename: destination of result file