#coding:utf-8
res = {}
res2=[]
res3=[]
with open('demo.txt') as f:
    for char in f.read().replace(' ', ''):
        if char in res:
            res[char] = res[char] + 1
        else:
            res[char] = 1
# mao pao fa qiu list_max3
res_list=res.items()
len=len(res_list)
for i in range(len-1):
    for j in range(len-1):
        if res_list[j][1]>res_list[j+1][1]:
            res_list[j],res_list[j+ 1]=res_list[j + 1],res_list[j]
print res_list
print res_list[-3:]