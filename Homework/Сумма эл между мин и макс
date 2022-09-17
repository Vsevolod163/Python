import random

def create_array(m):

    array = []
    
    for i in range(m):
        x = random.randint(1, 20)
        array.append(x)
    
    return array

def min_el(array):

    min_index = 0

    for i in range(len(array)):
        if array[i] < array[min_index]:
            min_index = i

    return min_index

def max_el(array):

    max_index = 0 

    for i in range(len(array)):
        if array[i] > array[max_index]:
            max_index = i

    return max_index

def sum_min_el_max_el(array, min_index, max_index): 
    
    sum = 0

    for i in range(len(array)):
        if i >= min_index and i <= max_index or i <= min_index and i >= max_index:  
            sum += array[i]

    return sum

x = create_array(5)
print(f"Массив: {x}")

a = min_el(x)
print(f"Минимальный элемент: {x[a]}")

b = max_el(x)
print(f"Максимальный элемент: {x[b]}")

c = sum_min_el_max_el(x, a, b)
print(f"Сумма: {c}")