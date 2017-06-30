# coding:utf-8
from pyquery import PyQuery as pq

url = 'https://movie.douban.com/top250'
# res = requests.get(url)

res=requests.get(url)
print res.text
