# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['book.douban.com/subject/1770782/']
    start_urls = ['http://book.douban.com/subject/1770782/']
    Pages=0

    def parse(self, response):
        title = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first('')
        self.Pages+=1
        comments_url = response.xpath('//div[@class="mod-hd"]/h2/span[2]/a/@href').extract_first('')
        header={
            'Referer':'https://book.douban.com/subject/1770782/',
            'Connection':'keep-alive'
        }
        if comments_url:
            Request(url=comments_url, meta={'Title': title},headers=header, callback=self.getcomments)

        pass
    def getcomments(self,response):

        self.Pages += 1
        comment = response.xpath('//div[@class="comment"]')
        # votes=comment[0].xpath('//h3/span[1]/span/text()').extract()
        # comments=comment[0].xpath('//h3/p/text()').extract()
        lines = []
        for i in comment:
            votes = i.xpath('h3/span[1]/span/text()').extract_first('')
            comments = i.xpath('p/text()').extract_first('')
            stars = i.xpath('h3/span[2]/span/@class').extract_first('')
            if stars == '':
                stars = '0'
            else:
                stars = stars[-9:-8]
            lines.append(comments + ',' + stars + ',' + votes + '\n')

        title=response.meta['Title']
        with open('{}.txt'.format(title),'a+')as f:
            for line in lines:
                f.writelines(line)

        next = response.xpath('//*[@id="content"]/div/div[1]/div/div[3]/ul/li[3]/a/@href').extract_first('')
        url = response.urljoin(next)
        if url and self.Pages < 15:
            yield Request(url, meta={'Title': title}, callback=self.getcomments)
            print('正在请求%d页数据'%self.Pages)
        pass

