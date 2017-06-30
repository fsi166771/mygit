#coding:utf-8
def jia(x,y):
    return x + y
def jian(x,y):
    return x - y
def cheng(x,y):
    return x * y
def chu(x,y):
    return x / y
incalc ={'+': jia,'_':jian,'*':cheng,'/':chu}
def f(x,o,y):
    print incalc.get(o)(x,y)
f(3,'*',2)