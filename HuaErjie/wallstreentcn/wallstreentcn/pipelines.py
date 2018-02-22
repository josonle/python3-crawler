# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class WallstreentcnPipeline(object):
    def process_item(self, item, spider):
        return item


class CSVPipeline(object):
    # def __init__(self):
    #     self.csvfile=open('HuaErJie_news.csv','w+',encoding='utf-8',newline='')
    #     self.writer=csv.writer(self.csvfile)
    #     self.writer.writerow(('快讯','时间','板块','id','name'))
    #     self.csvfile.close()

    def process_item(self,item,spider):
        if spider.name=='HuaErJie':
            print('Writing into HuaErJie.csv ,now...')
            with open('HuaErJie_news.csv', 'a+', encoding='utf-8', newline='')as f:
                writer = csv.writer(f)
                writer.writerow((item['time'], item['content'], item['channel'], item['id'], item['name']))
            return item
        if spider.name=='hejnews':
            print('Writing into hejnews.csv ,now...')
            with open('hejnews.csv','a+',encoding='utf-8',newline='')as f:
                writer=csv.writer(f)
                writer.writerow((item['title'],item['date_time'],item['author'],item['a_url'],item['content_short'],item['views'],item['categories'],item['url']))
            return item
        return item

class ProxyPipeline(object):

    def process_item(self,spider,item):
        with open('proxy.txt','a')as f:
            f.write(item['ip']+'\t')
            f.write(item['port']+'\t')
            f.write(item['type']+'\t')
            f.write(item['location']+'\t')
            f.write('\n')
        return item
