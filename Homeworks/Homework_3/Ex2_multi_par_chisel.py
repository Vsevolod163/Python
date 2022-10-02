# Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй и 
# предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def create_random_list(n):

    list1 = []

    for i in range(n):
        x = random.randint(-9, 9)
        list1.append(x)

    return list1

def multi(list):

    multi = 0
    list_of_multi = []

    if len(list) % 2 != 0:

        for i in range(int(len(list) / 2) + 1):
            
            if i == int(len(list) / 2):

                list_of_multi.append(list[i] ** 2) 

            else:

                multi = list[i] * list[-1 - i]
                list_of_multi.append(multi)
    else:

        for i in range(int(len(list) / 2)):

            multi = list[i] * list[-1 - i]
            list_of_multi.append(multi)

    return list_of_multi

list1 = create_random_list(5)
multi_of_el = multi(list1)

print(list1)
print(multi_of_el)
