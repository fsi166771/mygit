# conding:utf-8
names = ['aaaa', 'bb', 'ffff', 'fsafs', 's', 'sdf']
names2 = []
for name in names:
    if len(name) > 3:
        print name

names2 = [name for name in names if len(name) > 3]
print names2
#  转换为大写
#  names2 = [name.upper() for name in names if len(name) > 3]
# 不转换为大写
