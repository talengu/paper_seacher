# -*- coding: utf-8 -*-
import json
import os


# [first_name,second_name,year,name]
class SearchHelper(object):
    def __init__(self, in_txt_name):

        self.paper_list = self._read_txt(in_txt_name)

    def _read_txt(self, txt):
        lines = open(txt, 'r', encoding='UTF-8').readlines()
        res_list = []
        for line in lines:
            items = line.strip().split(',')

            name = ""
            for item in items[3:]:
                name += item
            [first_name, second_name, year] = items[0], items[1], items[2]
            res_list.append([first_name, second_name, year, name])
        return res_list

    def do_search(self, key):
        result_lis = []
        for items in self.paper_list:
            # 将单词变为low 方便索引
            # print(items)
            [first_name, second_name, year, name] = items
            if name.lower().find(key) != -1:
                result_lis.append(items)

        # 按照时间进行排序
        search_result = sorted(result_lis, key=lambda x: x[2], reverse=True)
        return search_result


# start = time.time()
# ....code
# end = time.time()
# print('Runs %0.2f seconds.' % (end - start))


if __name__ == "__main__":
    txt_path = '../paper_list/ai_papers.txt'
    n = SearchHelper(txt_path)

    key = 'relation'
    res = n.do_search(key)
    print(len(res), res)
