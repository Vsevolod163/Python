# Развернуть массив (Необязательно выводить каждый раз массив, метод PrintArray сделает это в следующих случаях (строка 29 выводит перевернутый массив))
import random

def ReverseArray(array):
    l = len(array) - 1
    # i = 0
    # while i < len(array) - i:
    #     temp = array[i]
    #     array[i] = array[l - i]
    #     array[l - i] = temp
    #     i += 1

    # return array

    for i in range(len(array)):
        if i < len(array) - i:
            temp = array[i]
            array[i] = array[l - i]
            array[l - i] = temp

    return array

def CreateArray(m):

    array = []

    for i in range(m):
        x = random.randint(0, 100)
        array.append(x)

    return array

def CreateArray2(m):

    array = [0] * m

    for i in range(m):
        array[i] = random.randint(0, 100)

    return array

array = CreateArray2(5)
print(array)
# array.reverse()
x = ReverseArray(array)
# print(array)
print(x)
