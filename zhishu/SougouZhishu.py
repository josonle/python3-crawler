import requests
import re
import json


class SougouZhishu(object):
	def __init__(self,searchwd):
		self.url='http://index.sogou.com/'
		self.params={
		'kwdNamesStr':searchwd,
		'timePeriodType':'MONTH',
		'dataType':'MEDIA_WECHAT',
		'queryType':'INPUT'
		}
		self.session=requests.Session()
	def get_main(self):
		header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Connection':'keep-alive',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Host':'index.sogou.com',
			'Referer':'http://index.sogou.com/'
			}
		url=self.url
		res=self.session.get(url,headers=header)
		# print(res.text)
		return res.status_code==200
	
	def get_index(self):
		header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Connection':'keep-alive',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Host':'index.sogou.com',
			'Referer':'http://index.sogou.com/'
			}
		url='http://index.sogou.com/index/media/wechat'
		params=self.params
		res=self.session.get(url,headers=header,params=params)
		# print(res.text)
		partten=re.compile(r'root.SG.data = (.*?);',re.S)
		content=re.findall(partten,res.text)[0]
		data=json.loads(content)
		dataList=[]
		# print(len(data['pvList'][0]),',',len(data['infoList'][0]))
		for i in data['pvList'][0]:
			#热度（点击量），相关文章，官方统计数，日期
			dataList.append((i['readTimes'],i['articleNum'],i['officialAccountsNum'],i['date']))
		return dataList
if __name__=='__main__':
	data=[]
	sougou=SougouZhishu('python')
	if sougou.get_main():
		data=sougou.get_index()
		for i in data:
			print(i)