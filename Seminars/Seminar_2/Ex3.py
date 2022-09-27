# Напишите программу, в которой пользователь будет задавать две 
# строки, а программа - определять количество вхождений одной строки 
# в другой.

x1 = str(input("Введите 1 строку: "))


x2 = str(input("Введите 2 строку: "))
count = 0

for i in range(len(x2) + 1):
    l = len(x1) + i
    if x1 == x2[i:l]: # срез берет в строке x2 от i элемента до l элемента
        count = count + 1
print(f"Результат: {count}")

print(x2.count(x1)) # готовый метод

# x1 = str(input("Введите 1 строку: "))
# def new_array(l):
#     array = []
#     for i in range(l):
#         x = str(input(f"Введите {i + 1} элемент: "))
#         array.append(x)

#     return array

# array = new_array(5)
# print(array)

# count = 0

# for i in range(len(array)):

#     if x1 == array[i]:
#         count = count + 1

# print(count)
