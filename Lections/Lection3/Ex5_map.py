li = [x for x in range(1, 20)]

print(li)

li = list(map(lambda x:x+10, li))

print(li)


data = list(map(int, input().split())) # по map можно пробижать 1 раз

print(data)