# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import  Request
import  re
from AticleSpider.items import AticlespiderItem

class DoubanreadSpider(scrapy.Spider):
    name = 'doubanread'
    # allowed_domains = ['book.douban.com/']
    start_urls = ['https://book.douban.com/top250']
    Pages=0#评论页数


    def parse(self, response):
        """
        1、 top250开始页面，获取每本书链接和推荐语（好像要用到meta）
        2、 每本书交给Request下载，并传给detail_parse解析
        3、 判断下一页是否存在，调用parse？
        """
        post_urls = response.xpath('//div[@class="indent"]/table/tr/td[2]/div/a/@href').extract()
        notes=response.xpath('//div[@class="indent"]/table/tr/td[2]/p/span/text()').extract()
        img_urls=response.xpath('//div[@class="indent"]/table/tr/td[1]/a/img/@src').extract()#可写成'//a[@class="nbg"]/img/@src'
        for url,note,img in zip(post_urls,notes,img_urls):
            print(response.url)
            print(url,note)
            yield Request(url=url,meta={'book_note':note,'book_img':img},callback=self.detail_parse)
            # break

        # next_url=response.xpath('//link[@rel="next"]/@href').extract_first('')
        # if next_url:
        #     yield  Request(url=next_url,callback=self.parse)

        pass

    def detail_parse(self,response):
        book_note=response.meta.get('book_note','')
        img_url=response.meta.get('book_img','')
        try:
            title = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first('')
            text = response.xpath('//*[@id="info"]/a[1]/text()').extract()[0].split('\n')
            author = text[-1].strip()
            if len(text) == 2:
                country = u'中国'
            else:
                country = text[1].strip()  #
            date = response.xpath('//*[@id="info"]').extract_first('')
            content = re.compile(r'<span class="pl">出版年:</span>(.*?)<br>', re.S)
            if re.findall(content, date):
                publish_date = re.findall(content, date)[0]
            else:
                publish_date = ''
            press = response.xpath('//*[@id="info"]/text()[5]').extract_first('').strip('')  # 出版社
            Score = float(response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first('').strip())  # 总评分数

            star = response.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[1]/@class').extract_first('')
            Star = float(re.match(r'.*?(\d+)', star).group(1)) / 10  # 平均星数

            participation_num = int(response.xpath('//a[@class="rating_people"]/span/text()').extract_first(''))  # 参与评分人次
            s = response.xpath('//span[@class="rating_per"]/text()').extract()
            s5 = float(s[0].strip('%')) / 100
            s4 = float(s[1].strip('%')) / 100
            s3 = float(s[2].strip('%')) / 100
            s2 = float(s[3].strip('%')) / 100
            s1 = float(s[4].strip('%')) / 100

        except:
            pass

        else:
            # 实例化items
            items = AticlespiderItem()
            items['title'] = title
            items['author'] = author
            items['country'] = country
            items['publish_date'] = publish_date
            items['note'] = book_note
            items['press'] = press
            items['Score'] = Score
            items['Star'] = Star
            items['People_nums'] = participation_num
            # items['s5'] = s5
            # items['s4'] = s4
            # items['s3'] = s3
            # items['s2'] = s2
            # items['s1'] = s1
            yield items

        # comments_url=response.xpath('//div[@class="mod-hd"]/h2/span[2]/a/@href').extract_first('')
        # if comments_url:
        #     pages=0
        #     yield Request(url=comments_url,meta={'Title':title ,'Pages':pages},callback=self.getcomments)
        #     print('{}请求评论。。。'.format(title))

        pass

    def getcomments(self,response):
        """
        1、 评论主要获取：短评、打分(有坑，有的人没有打分)、点赞数
        2、 txt保存，15页

        :param response:
        :return:
        """

        comment = response.xpath('//div[@class="comment"]')
        # votes=comment[0].xpath('//h3/span[1]/span/text()').extract()
        # comments=comment[0].xpath('//h3/p/text()').extract()
        lines=[]
        for i in comment:
            votes=i.xpath('h3/span[1]/span/text()').extract_first('')
            comments = i.xpath('p/text()').extract_first('')
            stars=i.xpath('h3/span[2]/span/@class').extract_first('')
            if stars=='':
                stars='0'
            else:stars=stars[-9:-8]
            lines.append(comments+','+stars+','+votes+'\n')
        title=response.meta['Title']
        with open('C:\\Users\\j\\Desktop\\comments\\{}.txt'.format(title),'a+',encoding='utf-8')as f:
            for line in lines:
                f.writelines(line)
        pages = response.meta['Pages']
        next=response.xpath('//*[@id="content"]/div/div[1]/div/div[3]/ul/li[3]/a/@href').extract_first('')
        url=response.urljoin(next)
        pages+=1
        while url :
            if pages<4:
                print('正在请求{}第{}页'.format(title, pages))
                yield Request(url, meta={'Title': title,'Pages':pages}, callback=self.getcomments)
                break
            else:
                print('{}超过{}页'.format(title,pages))
                break

        pass