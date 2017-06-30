#!/usr/bin/env python
# -*- coding: utf-8 -*-
menu=['a','b','c','d','e']
for x in range(5):
    for y in range(5):
        if not(x==y):
            print '{}{}'.format(menu[x],menu[y])
