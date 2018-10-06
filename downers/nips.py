import requests
from bs4 import BeautifulSoup
from downers.dblp_helper import BaseDowner, get_titles


def main_page_to_list(main_url='', first_name='', second_name=''):
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


def main():
    main_page_url = 'https://dblp.uni-trier.de/db/conf/nips/'
    name = 'nips'

    search_url_list = main_page_to_list(main_url=main_page_url,
                                        first_name=name.upper())
    aiDowner = BaseDowner(name, search_url_list)
    aiDowner.start_down_all()

    get_titles(name)


if __name__ == '__main__':
    main()
