from scrapy.cmdline import execute #调用这个可以执行scrapy脚本
import  sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))#找到工程目录才能运行scrapy命令，你可以打印一下看看
# print(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','HuaErJie'])
# execute(['scrapy','crawl','hejnews'])
execute(['scrapy','crawl','proxySpider'])
