# -*- coding: utf-8 -*-
import scrapy
import re
from GetProxy.items import ProxyItem
import urllib.request

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
            proxies = {type: '%s:%s' % (ip, port)}
            try:
                # 设置代理链接百度  如果状态码为200 则表示该代理可以使用 然后交给流水线处理
                proxy_support = urllib.request.ProxyHandler(proxies)
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)
                if urllib.request.urlopen('http://www.baidu.com').getcode() == 200:
                    print('%s 可用' % ip)
                    item = ProxyItem()
                    item['url'] = type + '://' + ip + ':' + port

                    yield item
            except:
                print('fail %s' % ip)
        pass
