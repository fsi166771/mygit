# coding:utf8
res ={}
with open('demo.txt') as f:
    for char in f.read().replace(' ',''):
        res[char]=res.get(char,0)+1
for c,num in sorted(res.items(),key=lambda x:-x[1])[:3]:
    print '%s count is %d'%(c,num)
