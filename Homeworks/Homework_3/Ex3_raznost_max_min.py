# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у 
# целых чисел дробной части нет их в расчет не берем

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01]

def float_list(list):

    new_list = []

    for i in range(len(list)):
        
        x = round(list[i] % 1, 2)

        if x > 0:
            new_list.append(x)
    
    return new_list

def min_el(list):

    index_min_el = 0

    for i in range(len(list)):
        if list[i] < list[index_min_el]:
            index_min_el = i

    return list[index_min_el]

def max_el(list):

    index_max_el = 0

    for i in range(len(list)):
        if list[i] > list[index_max_el]:
            index_max_el = i

    return list[index_max_el]

new_list = float_list(list1)

min = min_el(new_list)

max = max_el(new_list)

print(f'Начальный список: {list1}')
print(f'Список дробной части элементов > 0: {new_list}')

print(f'Минимальная дробная часть: {min}')
print(f'Максимальная дробная часть: {max}')

result = round(max - min, 2)

print(f'Разница между максимальной и минимальной дробной частью = {result}')