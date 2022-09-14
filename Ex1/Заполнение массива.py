import random

def create_2d_arr(m, n):
    
    array = []
    x = 0
    for i in range(m):
        array2 = []
        for j in range(n):
            x = random.randint(1, 20)
            array2.append(x)
        array.append(array2)

    return array

def print_2d_arr(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end = " ")
        print()

def check_element(array, el):

    count = 0

    for i in range(len(array)):
        for j in range((len(array[i]))):
            if array[i][j] == el:
                count += 1
    if count > 0:
        return True
    else:
        return False
    

x = create_2d_arr(3, 4)
print_2d_arr(x)



array2 = [[1, 2, 7], [5, 9, 1]]
print_2d_arr(array2)