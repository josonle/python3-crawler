# -*- coding: utf-8 -*-
import scrapy
import math
from scrapy.http import Request
from JianShu.items import JianshuItem

class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['https://www.jianshu.com/users/1fdc2f8e1b37/following']
    up_urls='https://www.jianshu.com/users/{id}/following'
    follow_urls='https://www.jianshu.com/users/{id}/following?page='
    id_set=set() #用于用户去重
    nums=0

    def parse(self, response):
        item=JianshuItem()

        try:
            item['name'] = response.xpath('//div[@class="main-top"]/div[@class="title"]/a/text()').extract_first('')
            up_id = response.xpath('//div[@class="main-top"]/div[@class="title"]/a/@href').extract_first('').split('/')[-1]
            self.id_set.add(up_id)
            item['id']=up_id
            print('开始解析{}'.format(item['name']))

            selector = response.xpath('//div[@class="main-top"]/div[@class="info"]/ul/li')
            # 关注的人
            num=int(selector[0].xpath('./div/a/p/text()').extract_first(''))
            item['following'] = num
            pages = math.ceil(num/10)#翻页pages
            # 粉丝
            item['follower'] = int(selector[1].xpath('./div/a/p/text()').extract_first(''))
            item['articles'] = int(selector[2].xpath('./div/a/p/text()').extract_first(''))  # 文章
            item['words'] = int(selector[3].xpath('./div/p/text()').extract_first(''))  # 字数
            item['likes'] = int(selector[4].xpath('./div/p/text()').extract_first(''))  # 收获喜欢
            # 作者简介
            item['introduction'] = response.xpath('//div[@class="description"]/div/text()').extract_first('')

        except:
            pass
        else:
            yield item
            for i in range(1, int(pages) + 1):
                up_url = self.follow_urls.format(id=up_id) + str(pages)
                self.nums+=1
                if self.nums>100:
                    break
                yield Request(url=up_url, callback=self.userlist_parse)
        pass
    def userlist_parse(self,response):
        urls=response.xpath('//div[@class="info"]/a[@class="name"]/@href').extract()
        url_list=[[self.up_urls.format(id=url_id.split('/')[-1]),self.id_set.add(url_id.split('/')[-1])] for url_id in urls if url_id not in self.id_set]
        # self.id_set.add(id.split('/')[-1]) for id in urls
        for url in url_list:
            yield Request(url=url[0], callback=self.parse)
