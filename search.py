from seachers.search_helper import SearchHelper


def fliter_year(item, key_year):
    [first_name, second_name, year, name] = item
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
    f = open(txt_out_name, 'w')
    for item in res_list:
        [first_name, second_name, year, name] = item

        f.write("%s,%s,%s,%s\n" % (first_name, second_name, year, name))
    f.close()


def generate(first_name="ECCV"):  # some 2018 year has not in the list
    res_list = []
    for line in open("ddd", 'r').readlines():
        name = line.strip()
        res_list.append([first_name, "", 2018, name])
    write(res_list, "tmp")


import glob

if __name__ == '__main__':

    key = 'relation'
    res_list = []
    for key_year in range(2018, 2010, -1):
        for txt_path in glob.glob(r"paper_list/*.txt"):
            tmp_list = search_one_txt(key, key_year, txt_path)
            res_list += tmp_list
        print(key_year, len(res_list))

    print(len(res_list))
    write(res_list, "relation.txt")

    # generate()
