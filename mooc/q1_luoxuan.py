#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import *  #在循环里不用写变量名字
import turtle  #需要定义变量名字对比程序Q1_luoxuan2.py
begin_fill()
for i in range(290):
    speed("fastest")
    forward(i*2)
    # forward(300 - (i + 10))
    right(90)
done()
