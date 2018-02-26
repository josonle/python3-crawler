# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
class LianjiaPipeline(object):
    def process_item(self, item, spider):
        return item

class CSVershouPipeline(object):
    def __init__(self):
        self.file=open('ErShouFang2.csv','w+',encoding='utf-8',newline='')
        self.writer=csv.writer(self.file)
        self.writer.writerow(['小区','户型','面积','地段','单价','总价','楼层','建成时间','有地铁'])
        self.file.close()
    def process_item(self,item,spider):
        with open('ErShouFang2.csv','a+',encoding='utf-8',newline='')as f:
            writer=csv.writer(f)
            writer.writerow([item['xiaoqu'],item['houseType'],item['meters'],item['location'],item['unitprice'],item['totalprice'],item['floor'],item['houseYear'],item['hasSubway']])

        return item
