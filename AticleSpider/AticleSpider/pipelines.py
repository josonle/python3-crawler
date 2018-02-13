# -*- coding: utf-8 -*-
import csv

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class CsvPipeline(object):
    def __init__(self):
        self.csvf=open('db_Top250.csv','a+',encoding='utf-8',newline='')
        self.writer=csv.writer(self.csvf)
        self.writer.writerow(
            ['书名', '作者', '国家', '荐语', '出版时间', '出版社', '评分', 'Star', '参与短评人次'])
        # self.writer.writerow(['书名','作者','国家','荐语','出版时间','出版社','评分','Star','参与短评人次','力荐','推荐','还行','较差','烂'])
        self.csvf.close()

    def process_item(self,item,spider):
        with open('db_Top250.csv','a+',encoding='utf-8 ')as f:
            writer=csv.writer(f)
            writer.writerow(
                [item['title'], item['author'], item['country'], item['note'], item['publish_date'], item['press'],item['Score'], item['Star'], item['People_nums']])
            # writer.writerow([item['title'],item['author'],item['country'],item['note'],item['publish_date'],item['press'],item['Score'],item['Star'],item['People_nums'],item['s5'],item['s4'],item['s3'],item['s2'],item['s1']])

        return item

class CSVPipeline(object):

  def __init__(self):
    self.files = {}

  @classmethod
  def from_crawler(cls, crawler):
    pipeline = cls()
    crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    return pipeline

  def spider_opened(self, spider):
    file = open('%s_items.csv' % spider.name, 'w+b')
    self.files[spider] = file
    self.exporter = CsvItemExporter(file)
    # self.exporter.fields_to_export = ['title','author','country','note','publish_date','press','Score','Star','People_nums']
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item


class JsonPipeline(object):
    def __init__(self):
        print('开始写入json')
        self.f=codecs.open('bookmessages.json','w',encoding='utf-8')
    def process_item(self,item,spide):
        lines=json.dumps(dict(item),ensure_ascii=False)
        self.f.write(lines+'\n')
        print('写入数据ing。。。')
        return item
    def spider_closed(self, spider):
        self.f.close()
        print('写入完成，文件关闭')