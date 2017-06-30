#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 乘阶运算
sum = 0
tmp = 1
for i in range(1, 11):
    tmp = tmp * i
    sum = sum + tmp
print'运算结果是：{}'.format(sum)
