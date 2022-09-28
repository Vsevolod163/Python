# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
from tkinter.filedialog import Open

def create_list(N):

    array = []

    for i in range(-N, N + 1):
        x = random.randint(-N, N)

        while check(array, x) == False:
            x = random.randint(-N, N)
        array.append(x)

    return array

def check(array, check_number):
    
    count = 0

    for i in range(len(array)):
        if array[i] == check_number:
            count += 1

    if count > 0:
        return False
    else:
        return True

array = create_list(3)
print(array)

file = open('/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_2/test.txt')

str1 = file.readline()
str2 = file.readline()
x1 = int(str1[5])
x2 = int(str2[5])
multi = int(array[x1]) * int(array[x2])
print(f'Произведение элементов на позициях {x1} и {x2} : {array[x1]} * {array[x2]} = {multi}')
