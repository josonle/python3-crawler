# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re,requests


class ZufangSpider(scrapy.Spider):
    name = 'zufang'
    allowed_domains = ['dl.lianjia.com/zufang']
    start_urls = ['http://dl.lianjia.com/zufang/']
    def start_requests(self):
        for url in self.start_urls:
            res=requests.get(url)
            content=re.compile(r'"totalPage":(.*?),"curPage"',re.S)
            pages=int(re.findall(content,res.content.decode('utf-8'))[0])
            print('共有%d页'%pages)
            for i in range(1,2):
                nexturl=url+'pg%d/'%i
                yield Request(url=nexturl,callback=self.parse)

    def parse(self, response):
        print(response.url+'租房')
        pass