# coding utf8
names = ['bob', 'tom', 'jerry', 'rose', 'jeck']
names2 = []
for name in names:
    if len(name) > 3:
        names2.append(name)
print names2
names3 = []
names3 = [name.upper() for name in names if len(name) > 3]
print names3
