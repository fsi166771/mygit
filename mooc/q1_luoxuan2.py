#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)  #笔的大小
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)   #3秒后自动关闭