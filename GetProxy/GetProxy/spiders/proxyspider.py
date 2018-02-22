# -*- coding: utf-8 -*-
import scrapy
import re
from GetProxy.items import ProxyItem
import urllib.request

class ProxyspiderSpider(scrapy.Spider):
    name = 'proxyspider'
    allowed_domains = ['www.swei360.com']
    url='http://www.swei360.com/free/?page='
    start_urls = []
    for i in range(1,2):
        start_urls.append(url+str(i))

    def parse(self, response):

        selector = response.xpath('//tbody//tr')
        for s in selector:
            # ip=s.xpath('./td[1]/text()').extract()[0]
            # port=s.xpath('./td[2]/text()').extract()[0]
            # type=s.xpath('./td[4]/text()').extract()[0]
            # #验证爬取的ip是否可用
            # proxies={type:ip+':'+port}
            # try:
            #     proxy_support = urllib.request.ProxyHandler(proxies)
            #     opener=urllib.request.build_opener(proxy_support)
            #     urllib.request.install_opener(opener)
            #     if urllib.request.urlopen('http://www.baidu.com').getcode()==200:
            #         print('%s 可用'%ip)
            # except:
            #     print('%s 不能用'%ip)


            item = ProxyItem()
            item['ip']=s.xpath('./td[1]/text()').extract()[0]
            item['port']=s.xpath('./td[2]/text()').extract()[0]
            item['type']=s.xpath('./td[4]/text()').extract()[0]
            item['location']=s.xpath('./td[5]/text()').extract()[0]
            yield item