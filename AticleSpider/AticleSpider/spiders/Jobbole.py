# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'Jobbole'         #启动项目scrapy crawl Jobbole
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://python.jobbole.com/83563/']       #注意这是个列表，可以用来放很多链接

    def parse(self, response):
        "/body/div[@class='entry-header']"
        # selector1=response.xpath('//*[@id="post-83563"]/div[1]/h1')
        # selector2 = response.xpath("//div[@class='entry-header']/h1/text()")
        title=response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]
        publish_date=response.xpath('//div[@class="entry-meta"]/p/text()').extract()[0].replace('· ','').strip()
        praise_num = response.xpath('//*[@id="83563votetotal"]/text()').extract()[0]#点赞数
        fav_num= int(re.findall(r'.*?(\d+).*?',response.xpath('//span[@data-item-id="83563"]/text()').extract()[0])[0])#收藏数
        #评论数，也可写作'//a[@href='#article-comment']/span/text()'
        comments_num=int(re.findall(r'.*?(\d+).*?',response.xpath('//*[@id="post-83563"]/div[3]/div[43]/a/span/text()').extract()[0])[0])

        pass
