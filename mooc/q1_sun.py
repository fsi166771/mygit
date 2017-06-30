#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import *

color('red','yellow')
begin_fill()
while True:
    forward(100)
    right(170)
    if abs(pos()) < 1:
        break
end_fill()
done()      #不会自动关闭