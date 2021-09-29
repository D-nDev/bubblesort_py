import random

randomlist = []
d = 500000
'''d = 10'''
for i in range(d):
    randomlist.append(random.randint(0, d))
    index = randomlist[-1]
    length = len(randomlist)
    if length > 1:
        for i in randomlist:
            if i > randomlist[-1]:
                getindex = randomlist.index(i)
                temp = randomlist[-1]
                randomlist[getindex] = temp
                randomlist[-1] = i

print(randomlist)
