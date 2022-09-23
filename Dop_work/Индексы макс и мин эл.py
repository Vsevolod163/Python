# Нахождение индексов максимального и минимального элемента массива

array = [1, 10, 7, -10]

def MinIndex(array):
    min_index = 0
    for i in range (len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index

def MaxIndex(array):
    max_index = 0
    for i in range (len(array)):
        if array[i] > array[max_index]:
            max_index = i
    return max_index

x1 = MinIndex(array)
x2 = MaxIndex(array)
print(f"Индекс минимального элемента = {x1}\nИндекс максимального элемента = {x2}")


