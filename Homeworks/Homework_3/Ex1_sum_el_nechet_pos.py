# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной 
# позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
# ответ: 12

import random

def create_random_list(n):

    list1 = []
    for i in range(n):
        x = random.randint(-9, 9)
        list1.append(x)

    return list1

def find_nechet_pos(list):

    sum = 0

    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]

    return sum

n = int(input('Введите количество элемента списка: '))

list1 = create_random_list(n)

sum_of_el = find_nechet_pos(list1)

print(f'Список: {list1}')
print(f'Сумма элементов на нечетных позициях = {sum_of_el}')
