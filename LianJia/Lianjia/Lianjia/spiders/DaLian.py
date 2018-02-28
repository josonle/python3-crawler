# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from Lianjia.items import LianjiaershouItem
import requests,re

class DalianSpider(scrapy.Spider):
    name = 'DaLian'
    allowed_domains = ['dl.lianjia.com']
    start_urls = [#'http://dl.lianjia.com/',
                  'https://dl.lianjia.com/ershoufang/',
                  # 'https://dl.lianjia.com/zufang/',
                  # 'https://dl.fang.lianjia.com/loupan/',
                  ]
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
        item=LianjiaershouItem()
        selector = response.xpath('//ul[@class="sellListContent"]//li[@class="clear"]/div[@class="info clear"]')
        for p in selector:
            try:

                item['xiaoqu'] = p.xpath('./div[@class="address"]/div/a/text()').extract_first('')
                item['houseType'] = p.xpath('./div[@class="address"]/div/text()').extract_first('').split('|')[1]
                item['meters'] = p.xpath('./div[@class="address"]/div/text()').extract_first('').split('|')[2]
                content = p.xpath('./div[@class="flood"]/div/text()').extract_first('')
                pattern = re.compile(r'共(.*?)层\)(.*?)年建')
                item['floor'], item['houseYear'] = re.findall(pattern, content)[0]
                item['floor']=int(item['floor'])
                item['houseYear']=int(item['houseYear'])
                item['location'] = p.xpath('./div[@class="flood"]/div/a/text()').extract_first('')
                item['totalprice'] = float(p.xpath('./div[@class="priceInfo"]/div[1]/span/text()').extract_first(''))
                item['unitprice'] = float(p.xpath('./div[@class="priceInfo"]/div[2]/@data-price').extract_first(''))
                item['hasSubway'] = True if p.xpath('./div[@class="tag"]/span[@class="subway"]') else False
            except Exception as e:
                print('信息不全，%s' % item['xiaoqu'])
                print('error:',e)
                print(item['xiaoqu'],item['houseType'],item['meters'],item['location'],item['unitprice'],item['totalprice'],item['floor'],item['houseYear'],item['hasSubway'])

            else:
                yield item
                print('%s爬取完成' % response.url)

        pass
