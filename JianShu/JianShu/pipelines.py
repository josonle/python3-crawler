# -*- coding: utf-8 -*-
#以下为自定义相应Pipeline所引入的模块
import csv

import json
import codecs#引入codecs模块解决编码问题

from scrapy.exporters import JsonItemExporter

import pymysql
import pymysql.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JianshuPipeline(object):
    def process_item(self, item, spider):
        return item
class CSVPipeline(object):
    def __init__(self):
        self.csvfile=open('JianShu_author_messages.csv','a+',encoding='utf-8',newline='')
        self.writer=csv.writer(self.csvfile)
        self.writer.writerow(('名','id','关注','粉丝','获得喜欢','文章','字数','个人简介'))
        self.csvfile.close()

    def process_item(self,item,spider):
        with open('JianShu_author_messages.csv','a+',encoding='utf-8',newline='')as f:
            writer=csv.writer(f)
            writer.writerow((item['name'],item['id'],item['following'],item['follower'],item['likes'],item['articles'],item['words'],item['introduction']))

        return item

class JsonEncodingPipeline(object):
    def __init__(self):
        print('start writing in files...')
        self.file = codecs.open('jianshu_author1.json', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        print('writing...')
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        print('ok,file is closed...')
        self.file.close()
class JsonExporterPipleline(object):
    #调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('jianshu_messsageexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
    # 打开文件
        self.exporter.start_exporting()
    # 导出文件

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    #  文件关闭

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

#同步使用PyMySQL链接数据库
class MySQLPipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(host='127.0.0.1',user='root',password='lzw2016609',db='jianshu',charset='utf8',use_unicode=True )
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        sql = 'insert into author_message(name,id,following,follower,likes,articles,words,introduction) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            # execute执行sql语句
            self.cursor.execute(sql, (item['name'], item['id'], item['following'], item['follower'], item['likes'],item['articles'],item['words'],item['introduction']))
            self.connect.commit()
            print('写入MySQL成功。。。')
        except Exception as e:
            print('insert error:',e)
    def close_spider(self):
        self.connect.close()


