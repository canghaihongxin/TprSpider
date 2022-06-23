#  execute 可以调用scrapy的执行脚本
from scrapy.cmdline import execute

import sys
import os

# print(os.path.dirname(os.path.abspath(__file__))) #获取当前文件所在的路径
# os.path.dirname(os.path.abspath(__file__)) 获取当前文件所在的父目录

if __name__ == '__main__':
    # 设置执行路径a
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # 设置执行命令
    execute(["scrapy", "crawl", "cnblogNews"])
