# -*- coding: utf-8 -*-
f1=open("text.txt","a")

f1.write("sbb\n")
# f1.read()
print f1
f1.close()
for i in file("text.txt"):
    print i