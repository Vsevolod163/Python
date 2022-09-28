# Реализуйте алгоритм перемешивания списка.

import random

def create_random_array(N):
    array = []

    for i in range(N):
        x = random.randint(-9, 9)
        while check(array, x) == False:
            x = random.randint(-9, 9)
        array.append(x)
    
    return array

def result_array(array):

    index_array = []
    new_array = []
    for i in range(len(array)):
        k = random.randint(0, len(array) - 1)
        
        while check(index_array, k) == False:  
            k = random.randint(0, len(array) - 1)
        index_array.append(k)

    for i in range(len(index_array)):
        x = index_array[i]
        j = array[x]
        new_array.append(j)
    
    return new_array

def check(array, check_number):
    
    count = 0

    for i in range(len(array)):
        if array[i] == check_number:
            count += 1

    if count > 0:
        return False
    else:
        return True

array = create_random_array(5)
print(f'Список: {array}')

x = result_array(array)
print(f'Перемешенный список: {x}')
