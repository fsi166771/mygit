#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import turtle
from turtle import *
# fillcolor('red')
# begin_fill()
# while True:
#     forward(200)
#     right(144)
#     if abs(pos())<1:
#         break
# end_fill()
#
#画一个三角 详细介绍 http://blog.csdn.net/fanfan4569/article/details/54784143
fillcolor('red')

begin_fill()
while True:
    forward(200)
    left(120)
    if abs(pos())<1:
        break
end_fill()