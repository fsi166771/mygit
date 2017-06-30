#mao pao qiu zui da 3ge

l=[('1',1111),('11',5111),('111',211),('1111',11),('11111',131),('111111',14),]
llen=len(l)
# print llen
for i in range(llen-1):

    for j in range(llen-1):
        if l[j][1]>l[j+1][1]:
            l[j],l[j+1]=l[j+1],l[j]
print l
print l[-3:]