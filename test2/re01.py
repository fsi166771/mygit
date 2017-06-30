# coding:utf-8
import re

from django.template.backends import django

r = r'^010-\d{8}'
s = re.findall(r, "010-54214845")
print s

rr = r'ab*'
ss = re.findall(rr, 'abbbbbb')
print ss

# 提取电话号码
r1 = r'\d{3,4}-?\d{8}'
sss = re.findall(r1, '0375-71689961')
print sss

p_tel = re.compile(r1)
kk = p_tel.findall('010-45125685')
print kk
django