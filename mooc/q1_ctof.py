#!/usr/bin/env python
# -*- coding: utf-8 -*-
#输入三次温度转换退出
for i in range(3):
    if i<3:
        val = raw_input('输入温度：')
        if val[-1] in ['C', 'c']:
            f = 1.8 * float(val[0:-1]) + 32
            print '转换后的温度为:%.2fF' % f
        elif val[-1] in ['F', 'f']:
            c = (float(val[0:-1]) - 32) / 1.8
            print '转换后的温度为:%.2fC' % c
        else:
            print '输入错误！'
        i += 1



