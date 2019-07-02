import requests
from bs4 import BeautifulSoup
from downers.dblp_helper import BaseDowner, get_titles


# journals 的 download 方法 PAMI https://dblp.uni-trier.de/db/journals/pami/
# Volume 41: 2019
def journals_main_page_to_list(main_url='', first_name='', second_name=''):
    # 返回对于这个主界面的子页面的东西
    # search_url_list [url, first_name , second_name ,year]
    search_url_list = []
    req = requests.get(url=main_url)
    html = req.text
    bf = BeautifulSoup(html)

    ul_tag = bf.find_all('ul')[-6]  # 这个-6是实际的结果

    for li in ul_tag.find_all('li'):
        year = (li.a.string).split(' ')[-1]  # 去掉最后的东西
        url = li.a['href']
        search_url_list.append([url, first_name, second_name, year])

    return search_url_list

# journals 的 download 方法 ijcv https://dblp.uni-trier.de/db/journals/ijcv/
# 2019: Volume 127
# 2018: Volume 126
# 2017: Volumes 121, 122, 123, 124, 125
def journals_main_page_to_list1(main_url='', first_name='', second_name=''):
    # 返回对于这个主界面的子页面的东西
    # search_url_list [url, first_name , second_name ,year]
    search_url_list = []
    req = requests.get(url=main_url)
    html = req.text
    bf = BeautifulSoup(html)

    ul_tag = bf.find_all('ul')[-6]  # 这个-6是实际的结果

    for li in ul_tag.find_all('li'):
        year = (li.get_text()).split(':')[0]  # 去掉最后的东西
        print(li.get_text())
        for a in li.find_all('a'):
            url = a['href']
            search_url_list.append([url, first_name, second_name, year])

    return search_url_list



# 会议的下载方法
def conf_main_page_to_list(main_url='', first_name='', second_name=''):
    # 返回对于这个主界面的子页面的东西
    # search_url_list [url, first_name , second_name ,year]
    search_url_list = []
    req = requests.get(url=main_url)
    html = req.text
    bf = BeautifulSoup(html)

    #####
    tags = bf.find_all('div', class_='data')
    for tag in tags:
        spans = tag.find_all('span')
        year = 0
        for span in spans:
            if span['itemprop'] == 'datePublished':
                year = span.string
        url = tag.find_all('a')[-1]['href']

        html_name = url.split('/')[-1]
        second_name = html_name.split('.')[0]

        search_url_list.append([url, first_name, second_name, year])
    #####
    return search_url_list


# def main(name = 'tip',
#          main_page_url = 'https://dblp.uni-trier.de/db/journals/tip/',
#          isjournal=True):
def main(name='icml',
         main_page_url='https://dblp.uni-trier.de/db/conf/icml/',
         isjournal=False):

    if isjournal:
        search_url_list = journals_main_page_to_list(main_url=main_page_url,
                                                     first_name=name.upper())
    else:
        search_url_list = conf_main_page_to_list(main_url=main_page_url,
                                                 first_name=name.upper())
    if name=='ijcv':
        search_url_list = journals_main_page_to_list1(main_url=main_page_url,
                                                     first_name=name.upper())

    aiDowner = BaseDowner(name, search_url_list)
    aiDowner.start_down_all()

    get_titles(name)


