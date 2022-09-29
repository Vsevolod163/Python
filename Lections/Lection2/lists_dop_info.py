list1 = [5, 2, 3, 4, 5]

list2 = list1

list1[0] = 123

list2[1] = 333 # меняет значения и в list1

for e in list1:
    print(e, end = ' ')

print()

for e in list2:
    print(e)

list1.pop() # удаляет последний эл списка

list1.pop(0) # удаляет определенный эл
print(list1)

list1.insert(2, 11) # добавляет эл в список на опред позицию (позиция, эл)

print(list1)

list1.append(1) # добавляет эл в конец списка

print(list1)