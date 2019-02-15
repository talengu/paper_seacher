# -*- coding: UTF-8 -*-


r"""
http://history.ccf.org.cn/sites/ccf/paiming.jsp

计算机图形学与多媒体
http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690854

人工智能
http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690839

人机交互与普适计算

http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690320
"""

from downers.downer import main as downloader

if __name__ == "__main__":
    downloader(name='tip',
               main_page_url='https://dblp.uni-trier.de/db/journals/tip/',
               isjournal=True)


