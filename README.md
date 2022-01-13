## Paper Seacher 

**NEW  202201** update all paper list !

where where where papers

This project is used for get names of papers of CCf-A, and a simple search function.



## List of Papers

### CV Focus

*Conference*
- CVPR: International Conference on Computer Vision and Pattern Recognition
- ICCV: International Conference on Computer Vision
- ECCV: European Conference on Computer Vision
- NIPS: Annual Conference on Neural Information Processing Systems
- ICLR: International Conference on Learning Representations
- ICML: International Conference on Machine Learning
- AAAI: AAAI Conference on Artificial Intelligence
- ACM MM: ACM International Conference on Multimedia
- IJCAI: International Joint Conference on Artificial Intelligence

| Name | papers_lists | dblp link |status|freq/year|
|--------|--------|--------|--------|--------|
| CVPR |   [2021-1988](paper_list/cvpr_papers.txt)   | [link](http://dblp.uni-trier.de/db/conf/cvpr/)  | OK |1/1|
| ICCV |   [2019-1988](paper_list/iccv_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/iccv/) [iccv2019](https://github.com/extreme-assistant/iccv2019/blob/master/ICCV2019_links.xlsx?raw=true) |  OK |1/2|
| ECCV |   [2020-1990](paper_list/eccv_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/eccv/) | OK |1/2|
|  |    |  |   ||
| NIPS |   [2020-1988](paper_list/nips_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/nips/)   [nips offical](https://papers.nips.cc/) | OK |1/1|
| ICML |   [2021-1988](paper_list/icml_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/icml/) [ICML2021 Oral](https://icml.cc/Conferences/2021/Schedule?type=Oral) | OK |1/1|
| ICLR |   [2021-2013](paper_list/iclr_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/iclr/) [OR openreview.net for ICLR 2021](https://openreview.net/group?id=ICLR.cc/2021/Conference)  | OK |1/1|
|  |    |  |   ||
| AAAI |   [2021-1980](paper_list/aaai_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/aaai/) | OK |1/1|
| ACM MM |   [2021-1993](paper_list/acmmm_papers.txt)|[link](https://dblp.uni-trier.de/db/conf/mm/)| OK |1/1|
| IJCAI |   [2021-1969](paper_list/ijcai_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/ijcai/) | OK  |1/1|



*Journal*

- TPAMI: IEEE Trans on Pattern Analysis and Machine Intelligence
- IJCV: International Journal of Computer Vision
- TIP: IEEE Transactions on Image Processing

| Name | papers_lists | dblp link |status|freq/year|
|--------|--------|--------|--------|--------|
| PAMI |   [2022-1979](paper_list/pami_papers.txt)    | [link](http://dblp.uni-trier.de/db/journals/pami/) | OK |1/1|
| IJCV |   [2021-1987](paper_list/ijcv_papers.txt)    | [link](http://dblp.uni-trier.de/db/journals/ijcv/) | OK |1/1|
| TIP |   [2019-1992](paper_list/tip_papers.txt)    | [link](https://dblp.uni-trier.de/db/journals/tip/) |  OK |1/1|





## TODO
- [ ] can auto download papers 
- [ ] can search the context of papers
- [ ] can get cite index from google
- [ ] show oral or poster
- [ ] show author background
- [ ] show pdf link and code link
- [ ] have a front webview

## My List

keyword="relation" year>=2017

- [relation.txt](my_lists/relation.txt)
- [attention.txt](my_lists/attention.txt)
- [object detection.txt](my_lists/object_detection.txt)
- [gan.txt](my_lists/gan.txt)


### How to use this project

```bash
$ cd this project root
$ python3 search.py --keys attentions,relations --outpath my_lists/
# --keys use , to split
# --outpath to save papers_list
```



### Maybe there is a simple way? wahaha . . .

```
keyword=?????
https://dblp.uni-trier.de/search/publ?q={keyword} venue:CVPR|ICCV|ECCV|AAAI|ICML|NIPS|IJCAI year:2019|2018|2017

Google https://scholar.google.com
ieee https://ieeexplore.ieee.org/search/advsearch.jsp
ACM https://dl.acm.org/advsearch.cfm
arxiv https://arxiv.org/search/advanced

```

## Where Good
[CCF 人工智能](https://www.ccf.org.cn/xspj/rgzn/)
[CCF 计算机图形学与多媒体 ](https://www.ccf.org.cn/xspj/jsjtxxydmt/)
[CCF 人机交互与普适计算](https://www.ccf.org.cn/xspj/rjjhypsjs/)

[CCF-A](ccf.md)



Thanks for python module [beautifulsoup](http://beautifulsoup.readthedocs.io/zh_CN/latest/)

