# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from curses.ascii import isdigit


path1 = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_4/Ex5_file1'
path2 = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_4/Ex5_file2'


with open(path1) as file1:
    
    for i in file1:
        list1 = i.split(' ')
    # print(list1)
   

with open(path2) as file2:

    for i in file2:
        list2 = i.split(' ')
    # print(list2)

# Выводим строку с коэффициентами

res1 = ''
for i in range(0, len(list1), 2):
    
    for j in range(len(list1[i])):
        if list1[i][0].isdigit() == False:
            res1 += '1 '
            break
        if list1[i][j].isdigit():
            res1 += list1[i][j]
        else:
            
            res1 += ' '
            break
    
# print(res1)

# Список знаков 1

list_7 = []

for i in range(1, len(list1) - 2, 2):
    list_7.append(list1[i])

# print(list_7)

# Выводим строку без лишних цифр

a = res1[0:-1]
# print(a)

# Записываем коэфы в список

k = a.split(' ')
# print(k)

# Убираем пробелы из списка

new_list2 = []

for i in k:
    if i != '':
        new_list2.append(i)

for i in range(len(list_7)):
    if list_7[i] == '-':
        new_list2[i + 1] = -int(new_list2[i + 1])
        
# print(new_list2)

# Записываем степени в список

new_list3 = []

res2 = ''

for i in range(0, len(list1), 2):
    
    for j in range(len(list1[i])):
        
        if list1[i][len(list1[i]) - j - 1].isdigit():
            res2 = res2 + list1[i][len(list1[i]) - j - 1]
            
        else:
            
            res2 += ' '
            break
        
# print(res2)

a3 = res2[0:-1]
# print(a3)

# Записываем коэфы в список

k3 = a3.split(' ')
# print(k3)

# Убираем пробелы из списка

new_list4 = []

for i in k3:
    if i != '':
        new_list4.append(i)

# print(new_list4)

# Сопоставляем степени(ключи) со значениями коэфов

d3 = {}

for i in range(len(new_list2)):
    d3[new_list4[i]] = int(new_list2[i])

print(d3)

# Делаем для второго уравнения

res3 = ''
for i in range(len(list2)):
    
    for j in range(len(list2[i])):
        if list2[i][0].isdigit() == False:
            res1 += '1 '
            break
        if list2[i][j].isdigit():
            res3 += list2[i][j]
        else:
            res3 += ' '
            break
# print(res3)

# Список знаков 2 

list_8 = []

for i in range(1, len(list2) - 2, 2):
    list_8.append(list2[i])

# print(list_8)
# Выводим строку без лишних цифр

a1 = res3[0:-2]
# print(a1)


# Записываем коэфы в список

k1 = a1.split(' ')
# print(k1)

# Убираем пробелы из списка

new_list5 = []

for i in k1:
    if i != '':
        new_list5.append(i)


for i in range(len(list_8)):
    if list_8[i] == '-':
        new_list5[i + 1] = -int(new_list5[i + 1])
        
# print(new_list5)

# Записываем степени в список

new_list6 = []

res4 = ''
for i in range(len(list2)):
    
    for j in range(len(list2[i])):
        if list2[i][len(list2[i]) - j - 1].isdigit():
            res4 = res4 + list2[i][len(list2[i]) - j - 1]
        else:
            res4 += ' '
            break

# print(res4)
a4 = res4[0:-1]
# print(a4)

# Записываем коэфы в список

k4 = a4.split(' ')
# print(k4)

for i in k4:
    if i != '':
        new_list6.append(i)

# print(new_list6)

# Убираем пробелы из списка

new_list7 = []

for i in range(len(new_list6)):
    if new_list6[i] != '':
        new_list7.append(new_list6[i])

# print(new_list7)

# Сопоставляем степени(ключи) со значениями коэфов

d4 = {}

for i in range(len(new_list5)):
    d4[new_list7[i]] = int(new_list5[i])

print(d4)

# Сложение словарей

d5 = d3

for key, value in d4.items():
    if key in d3:
        d5[key] += value
    else:
        d5.update({key: value})
 
# print(d5)

k = ''

sorted_dict = {k: v for k, v in sorted(d5.items())}
items = list(sorted_dict.items())
sorted_dict2 = {k: v for k, v in reversed(items)}
print(sorted_dict2)

for key, value in sorted_dict2.items():
    
    if value == - 1:
        k += f'- x^{key} '
    elif value == 1:
        k += f'+ x^{key} '
    elif value < 0:
        k += f'- {-value}x^{key} '
    else:
        k += f'+ {value}x^{key} '
       
else:
    k += '= 0'

print(k[2:]) 

path3 = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_4/Ex5_resultfile'

with open(path3, 'w') as list3:
    list3.write(k[2:])