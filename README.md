## Paper Seacher

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

| Name | papers_lists | dblp link |status|
|--------|--------|--------|--------|
| CVPR |   [2019-1988](paper_list/cvpr_papers.txt)   | [link](http://dblp.uni-trier.de/db/conf/cvpr/) [cvpr2019](my_lists/cvpr2019.xlsx) | OK |
| ICCV |   [2017-1988](paper_list/iccv_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/iccv/) | OK |
| ECCV |   [2018-1990](paper_list/eccv_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/eccv/) | OK |
|  |    |  |   |
| NIPS |   [2018-1988](paper_list/nips_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/nips/) | OK |
| ICML |   [2018-1988](paper_list/icml_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/icml/) | OK  |
| ICLR |   [2018-2013](paper_list/iclr_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/iclr/) [ICLR 2019](https://openreview.net/group?id=ICLR.cc/2019/Conference)  | working  |
|  |    |  |   |
| AAAI |   [2018-1980](paper_list/aaai_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/aaai/) | OK |
| ACM MM |   [2018-1993](paper_list/acmmm_papers.txt)|[link](https://dblp.uni-trier.de/db/conf/mm/)| OK |
| IJCAI |   [2018-1969](paper_list/ijcai_papers.txt)    | [link](https://dblp.uni-trier.de/db/conf/ijcai/) | OK  |



*Journal*

- TPAMI: IEEE Trans on Pattern Analysis and Machine Intelligence
- IJCV: International Journal of Computer Vision
- TIP: IEEE Transactions on Image Processing

| Name | papers_lists | dblp link |status|
|--------|--------|--------|--------|
| PAMI |   [2019-1979](paper_list/pami_papers.txt)    | [link](http://dblp.uni-trier.de/db/journals/pami/) | OK |
| IJCV |   [2019-1987](paper_list/ijcv_papers.txt)    | [link](http://dblp.uni-trier.de/db/journals/ijcv/) | OK |
| TIP |   [2019-1992](paper_list/tip_papers.txt)    | [link](https://dblp.uni-trier.de/db/journals/tip/) |  OK |





## TODO
- [ ] can auto download papers 
- [ ] can search the context of papers

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

