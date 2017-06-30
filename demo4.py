res = {}
with open('demo.txt') as f:
    for char in f.read().replace(' ', ''):
        if char in res:
            res[char] = res[char] + 1

        else:
            res[char] = 1
print res
