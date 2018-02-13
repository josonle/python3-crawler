#新建main文件，用来设置断点调试程序
#在其他py文件上打上断点后，debug该main文件即可
from scrapy.cmdline import execute
import  sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','Jobbole'])#这其实就是scrapy启动项目的命令拆分
execute(['scrapy','crawl','doubanread'])