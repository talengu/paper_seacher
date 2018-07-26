import requests
from bs4 import BeautifulSoup
from downers.dblphelper import BaseDowner


def main_page_to_list(main_url='', first_name='', second_name=''):
    # 返回对于这个主界面的子页面的东西
    # search_url_list [url, first_name , second_name ,year]
    search_url_list = []
    req = requests.get(url=main_url)
    html = req.text
    bf = BeautifulSoup(html)

    #####
    ul_tag = bf.find_all('ul')[-6]  # 这个-6是实际的结果

    for li in ul_tag.find_all('li'):
        year = (li.contents[0]).split(':')[0]  # 去掉最后的东西
        for a in li.find_all('a'):
            url = a['href']
            search_url_list.append([url, first_name, second_name, year])
    #####
    return search_url_list


def main():
    main_page_url = 'https://dblp.uni-trier.de/db/journals/ai/'
    name = 'ai'

    search_url_list = main_page_to_list(main_url=main_page_url,
                                        first_name='AI')
    aiDowner = BaseDowner(name, search_url_list)
    aiDowner.start_down_all()


if __name__ == '__main__':
    main()
