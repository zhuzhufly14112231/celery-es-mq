#!/usr/bin/env python
# encoding: utf-8
'''
@file: es_orm.py
@time: 2018/11/9 9:32
'''
import datetime
from urllib.request import Request,urlopen
from lxml import etree
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document,Text,Keyword,Date,Integer

# 定义一个默认的es的client
es = connections.create_connection(hosts=['localhost'])
a=es.search(index='blog1',doc_type='doc',body={
  "query": {
    "bool": {
      "should": [
        {"term": {
          "title": {
            "value": "十月"
          }
        }},
        {"term": {
          "body": {
            "value": "事件"
          }
        }}
      ]
    }
  },
  "highlight": {
    "fields": {
      "title":{},
      "body":{}
    }
  },
  "from": 0
  , "size": 20
})
print(a)
class Artical(Document):
    title = Text(analyzer='ik_max_word')
    body = Text(analyzer='ik_max_word')
    href = Text()
    # title = Text(analyzer='ik_max_word')
    # body = Text(analyzer='ik_max_word')
    # tag = Keyword()
    # publish_from = Date()
    # vote = Integer()

    class Index:
        name = 'blog1'
        settings = {"number_of_shards":2}


# Artical.init()


# 添加数据
# article = Artical(meta={'id':1},title='First_es',body='hello es',tag=['es'],publish_from=datetime.datetime.now(),vote=111)
# article.save()

# 查询数据
# article = Artical.get(id=1)
# article.tag = ['hello','world']1
# article.save()
# 删除数据
# article.delete()

class Spider(object):
    def __init__(self):
        self.base_url = 'https://www.jianshu.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def load_url(self):
        request = Request(self.base_url,headers=self.headers)
        response = urlopen(request)
        code = response.read()
        root = etree.HTML(code)
        article_list = root.xpath('//div[@id="list-container"]/ul/li')
        for article in article_list:
            title = article.xpath('.//div[@class="content"]/a/text()')[0]
            href = article.xpath('.//div[@class="content"]/a/@href')[0]
            id = article.xpath('.//@data-note-id')[0]
            article_url = self.base_url + href
            article_request = Request(article_url,headers=self.headers)
            response = urlopen(article_request)
            article_code = response.read().decode()
            article_root = etree.HTML(article_code)
            article_text = article_root.xpath('//div[@class="show-content-free"]//p/text()')
            es_article = Artical(meta={'id':id},title=title,body=article_text,href=article_url)
            es_article.save()

# spider = Spider()
# spider.load_url()






























