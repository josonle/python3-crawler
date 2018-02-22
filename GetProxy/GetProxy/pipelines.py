# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class GetproxyPipeline(object):
    def process_item(self, spider, item):
        return item


# class TxtproxyPipeline(object):
#     def process_item(self, spider, item):
#         with open('proxy.txt', 'a')as f:
#             ip=item['ip']
#             port=item['port']
#             f.write(ip + '\t')
#             f.write(port + '\t')
#             # f.write(item['type'].encode('utf-8') + '\t')
#             # f.write(item['location'].encode('utf-8') + '\t')
#             f.write('\n')
#         return item

class TxtproxyPipeline(object):
    def __init__(self):
        self.file = open('proxy.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(item['ip']+'\t')
        self.file.write(item['port']+'\t')
        self.file.write(item['type']+'\t')
        self.file.write(item['location']+'\n')
        return item


    def close_spider(self, spider):
        self.file.close()
        pass
class ProxyPipeline(object):
    def __init__(self):
        self.file=open('proxy.json','w',encoding='utf8')

    def process_item(self,item,spider):
        line=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
