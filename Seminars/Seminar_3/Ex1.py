# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число и 
# вывести индекс строки.

def create_string_array(N):
    my_list = []
    for i in range(N):
        x = input(f"Введите {i} элемент: ")
        my_list.append(x)

    return my_list

def check_number_in_list(array, x):
    
    list1 = []
    for i in range(len(array)):
        for j in array[i]:
            if j == str(x):
                list1.append(i)

    return list1


a = input("Введите число: ")
array = create_string_array(3)
print(array)

x = check_number_in_list(array, a)
print(x)