from random import randint as r

mylist = ''.join(list(map(str, [r(0, 9) for i in range(20)])))

print(mylist)

unique = {}

for c in mylist:
    if unique.get(c):
        unique[c] = unique.get(c) + 1

    else:
        unique[c] = 1

uList = []

for i in unique.items():
    if i[1] == 1:
        uList.append(i[0])

print(uList)