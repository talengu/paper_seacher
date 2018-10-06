# -*- coding: UTF-8 -*-
r"""This base tools for down and cache the dblp
code help ref: http://beautifulsoup.readthedocs.io/zh_CN/latest/
"""
import os
import time
from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests

down_root = 'down_pages'


def saveFile(soup, save_path):
    f_obj = open(save_path, 'wb')  # wb 表示打开方式,也可用w
    for text in soup.find_all('div', class_='data'):
        f_obj.write("#".encode('utf-8'))
        f_obj.write(text.encode('utf-8'))
    f_obj.close()


def down_url(url):
    down_root = 'down_pages'
    items = url.split('/')
    save_path = os.path.join(down_root, items[-2], items[-1])
    if not os.path.isdir(os.path.join(down_root, items[-2])):
        os.makedirs(os.path.join(down_root, items[-2]))
    if not os.path.isfile(save_path):
        req = requests.get(url)
        html = req.text
        bf = BeautifulSoup(html)
        saveFile(bf, save_path)
        print(save_path)
        return save_path
    else:
        return save_path


def long_time_task(url):
    print('Run task %s (%s)...' % (url, os.getpid()))
    start = time.time()
    down_url(url)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (url, (end - start)))


def down_all(search_url_list):
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for item in search_url_list:
        url = item[0]
        p.apply_async(long_time_task, args=(url,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


class BaseDowner(object):
    def __init__(self, name, search_url_list):
        self.name = name
        self.search_url_list = search_url_list
        # fun_main_page_to_list must return search_url_list

    def _write_to_txt(self, out_txt_path, search_url_list):
        if not os.path.exists(down_root):
            os.makedirs(down_root)
        f = open(out_txt_path, 'w')
        for items in search_url_list:
            f.write("%s,%s,%s,%s\n" % (items[0], items[1], items[2], items[3]))
        f.close()

    def _read_from_txt(self):
        txt_path = os.path.join(down_root, self.name + '.txt')
        search_url_list = []
        if os.path.isfile(txt_path):
            f = open(txt_path, 'r')
            for line in f.readlines():
                items = line.split(',')
                search_url_list.append([items[0], items[1], items[2], items[3]])
        else:
            search_url_list = self.search_url_list
            self._write_to_txt(txt_path, self.search_url_list)

        return search_url_list

    def start_down_all(self):
        down_all(self._read_from_txt())


r"""当下载完成后使用下面得方法生成paper_list
"""


def singe_page(url):
    # url="https://dblp.uni-trier.de/db/journals/tip/tip27.html"
    # 不保存的做法
    # req = requests.get(url=ccf_ai)
    # html = req.text
    # bf = BeautifulSoup(html)
    # texts = bf.find_all('div', class_='data')

    # 保存文件不用重新下载
    htmlfile = open(down_url(url), 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    bf = BeautifulSoup(htmlhandle)
    texts = bf.find_all('div', class_='data')

    title_list = []
    for text_tag in texts:
        title_list.append(text_tag.find_all('span', class_='title')[0].string)
    return title_list


def get_titles(name):
    txt_path = os.path.join(down_root, name + '.txt')
    res_list = []
    f = open(txt_path, 'r')
    fw = open('paper_list/' + name + '_papers.txt', 'w', encoding='utf-8')
    for line in f.readlines():
        items = line.split(',')
        title_list = singe_page(url=items[0])
        print(line)
        for title in title_list:
            first_name = items[1]
            second_name = items[2]
            year = items[3][:-1]
            res_list.append([first_name, second_name, year, title])
            fw.write("%s,%s,%s,%s\n" % (first_name, second_name, year, title))
    fw.close()
    f.close()
    return res_list
