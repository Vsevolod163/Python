# Сумма элементов на нечетных позициях в списке
import random

list1 = [random.randint(-10, 10) for _ in range(5)]
print(list1)

print(f'Сумма элементов на нечетных позициях = {sum([list1[i] for i in range(len(list1)) if i % 2 != 0])}')

a = list(enumerate(list1))

res = sum([a[i][1] for i in range(len(a)) if i % 2 != 0])
print(f'Сумма элементов на нечетных позициях через enumerate = {res}')
