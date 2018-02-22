### 华尔街见闻

#### [实时快讯](https://wallstreetcn.com/live/global)：

https://wallstreetcn.com/live/global

分为六大板块：宏观，区块链，A股，美股，外汇，商品

ajax动态加载

api接口：https://api-prod.wallstreetcn.com/apiv1/content/lives/pc?limit=40

对应items参数：global,blockchain,a_stock,us_stock,forex ,commodity

limit参数控制返回多少条信息

#### [资讯](https://wallstreetcn.com/news/global?from=navbar):

https://wallstreetcn.com/news/global?from=navbar

分为：最新（包含后者），股市,商品，中国，美国，欧洲，日本，数据,经济

对应api接口:

'https://api-prod.wallstreetcn.com/apiv1/content/articles?category={}&limit=20&platform=wscn-platform'
'global','shares','commodities','china','us','europe','japan','charts','economy'

对应items参数：'global','shares','commodities','china','us','europe','japan','charts','economy'

**还包含一个cursor参数**，对应上一条新闻到当前新闻的时间戳（由next_cursor返回） 
 
PS：cursor=1518586780,1518422967 https://api-prod.wallstreetcn.com/apiv1/content/articles?category=commodities&limit=40&cursor=1518586780,1518422967&platform=wscn-platform

How can I use different pipelines for different spiders in a single Scrapy project
如何在一个scrapy运行多个spider时指定相对应的pipeline
https://stackoverflow.com/questions/8372703/how-can-i-use-different-pipelines-for-different-spiders-in-a-single-scrapy-proje/34647090#34647090

[伤神的博客](http://www.shangyang.me/2017/07/25/scrapy-learning-9-item-pipeline/#from-crawler-cls-crawler)

[scrapy如何针对不同的spider指定不同的参数](http://blog.csdn.net/qzc295919009/article/details/42737589)