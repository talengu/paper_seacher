# -*- coding: utf-8 -*-
# talen@uestc 
# 2019-07-02
import glob
import argparse
import sys
import os

sys.path.append("./seachers")
from seachers.search_helper import SearchHelper


def fliter_year(item, key_year):
    [first_name, second_name, year, name] = item

    # 防止ValueError: invalid literal for int() with base 10: '1988/1989'
    if len(year) > 4:
        m_years = year.split('/')
        year = int(m_years[0])
    else:
        year = int(year)

    if year == key_year:
        return 1
    else:
        return 0


def search_one_txt(key, key_year, txt_path):
    # search key in one txt
    n = SearchHelper(txt_path)

    tmp_list = n.do_search(key)  # do_search funs can be rewrite
    res_list = []
    for item in tmp_list:
        if fliter_year(item, key_year):  # TODO: in here can add some filters
            res_list.append(item)

    return res_list


def write(res_list, txt_out_name):
    f = open(txt_out_name, 'w', encoding='UTF-8')
    for item in res_list:
        [first_name, second_name, year, name] = item

        f.write("%s,%s,%s,%s\n" % (first_name, second_name, year, name))
    f.close()


def generate_my_list(key="", out_path=""):
    res_list = []
    for key_year in range(2020, 2016, -1):
        for txt_path in glob.glob(r"paper_list/*.txt"):
            tmp_list = search_one_txt(key, key_year, txt_path)
            res_list += tmp_list
            # print(key_year, len(res_list))

    print(key, len(res_list))
    write(res_list, "%s/%s.txt" % (out_path, key.replace(' ', '_')))


def generate(first_name="ECCV"):  # some 2018 year has not in the list
    res_list = []
    for line in open("ddd", 'r', encoding='UTF-8').readlines():
        name = line.strip()
        res_list.append([first_name, "", 2018, name])
    write(res_list, "tmp")


parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--keys', type=str, default="relation,attention,object detection,generate,gan,image,expression,image synthesis,image generate,facial expression")
parser.add_argument('--outpath', type=str, default="my_lists")
args = parser.parse_args()


def main():
    print("key: " + args.keys, "outpath: " + args.outpath)
    for key in args.keys.strip().split(','):
        if not os.path.exists(args.outpath):
            os.makedirs(args.outpath)
        generate_my_list(key, args.outpath)

        # generate()


if __name__ == '__main__':
    main()
