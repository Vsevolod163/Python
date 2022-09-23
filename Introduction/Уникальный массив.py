import random

def CreateArray(m):

    array = []

    for i in range(m):
        x = random.randint(1, 5)
        while Check(array, x) == True:
            x = random.randint(1, 5)
        array.append(x)

    return array

def PrintArray(array):
    for i in array:
        print(i, end = ' ')

def Check(array, el):
    
    count = 0

    for i in array:
        if i == el:
            count += 1
    if count > 0:
        return True
    else:
        return False

array = CreateArray(5)
PrintArray(array)