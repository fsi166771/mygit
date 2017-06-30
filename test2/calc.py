#coding:utf-8
def jia(x,y):
    return x + y
def jian(x,y):
    return x - y
def cheng(x,y):
    return x * y
def chu(x,y):
    return x / y

def incalc(x,o,y):
    if o == "+":
        print jia(x,y)
    elif o == '_':
        print jian(x,y)
    elif o == '*':
        print cheng(x,y)
    elif o == "/":
        print chu(x,y)
    else:
        pass

incalc(2.0,"/",22)
incalc(22,'/',22)
print jia