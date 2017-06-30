#!/usr/bin/env python
# -*- coding: utf-8 -*-
n=1
for i in range(5,0,-1):
    # 意思是n+1的二进制位数向左移动1位，最右位补0，相当于(n+1)*2
    #左移，二进制左移，相当于乘2
    n=(n+1)<<1
    print n