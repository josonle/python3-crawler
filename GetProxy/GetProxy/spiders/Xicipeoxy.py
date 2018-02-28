# -*- coding: utf-8 -*-
import scrapy
from GetProxy.items import ProxyItem
# import urllib.request
import requests

class XicipeoxySpider(scrapy.Spider):
    name = 'Xicipeoxy'
    allowed_domains = ['www.xicidaili.com/nn/']
    start_url='http://www.xicidaili.com/nn/'
    start_urls = []
    for i in range(1,4):
        start_urls.append(start_url+str(i))

    def parse(self, response):
        # 提取出ip列表
        ip_list = response.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[2]/text()').extract()
        # 提取出端口列表
        port_list = response.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[3]/text()').extract()
        # 提取出协议类型列表
        type_list = response.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[6]/text()').extract()
        print(response.url)
        for (ip, port, type) in zip(ip_list, port_list, type_list):
            proxies = {'http': 'http://%s:%s/' % (ip, port)}
            #以下是使用urllib添加代理
            # proxy_support = urllib.request.ProxyHandler(proxies)
            # opener = urllib.request.build_opener(proxy_support)
            # urllib.request.install_opener(opener)
            try:
                #检验网址'http://2017.ip138.com/ic.asp'或'http://httpbin.org/ip'
                # req=urllib.request.Request('http:httpbin.org/ip')
                # res=urllib.request.urlopen(req,timeout=30)
                #这里是使用requests添加代理，更简单
                res=requests.get('http://httpbin.org/ip',proxies=proxies,timeout=15).content.decode('utf-8')
                print('%s 可用,  %s' % (ip,res))
                item = ProxyItem()
                item['url'] = type + '://' + ip + ':' + port
                yield item
            except Exception as e:
                print('Error:',e)
                print('fail %s' % ip)
        pass
