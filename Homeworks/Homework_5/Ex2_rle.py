# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

from curses.ascii import isdigit


def sjatie(list1):

    rle_list = ''
    count = 0

    for i in range(len(list1)):
        if i + 1 == len(list1) - 1 and list1[i] == list1[i + 1]:
            rle_list += (f'{count + 2}{list1[i]}')
            break
        elif i + 1 == len(list1) - 1 and list1[i] != list1[i + 1]:
            rle_list += f'{count + 1}{list1[i]}'
            rle_list += f'1{list1[-1]}'
            break
        elif list1[i] == list1[i + 1]:
            count += 1
        elif list1[i] == '\n':
            rle_list += '\n'
        else:
            rle_list += f'{count + 1}{list1[i]}'
            count = 0
    
    return rle_list


def data_module(file1_list):

    rle_list = ''
    for i in range(len(file1_list)):
        if file1_list[i][0].isdigit() == False:
            if i == len(file1_list) - 1:
                rle_list += sjatie(file1_list[i])
            else:
                rle_list += sjatie(file1_list[i]) + '\n'
        else:
            if i == len(file1_list) - 1:
                x = 'Super!'
                rle_list += x
            else:
                x = 'Super!'
                rle_list += x + '\n'
    
    return rle_list

path1 = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_5/ex2_data_file'

with open(path1) as file1:
    str1 = ''
    for line in file1:
        for j in line:
            str1 += j

file1_list = str1.split('\n')
print(file1_list)

result = data_module(file1_list)
print(result)


str2 = '11a3b7c'

res2 = ''
for i in range(len(str2)):
    if str2[i].isdigit():
        res2 += str2[i]
    else:
        res2 += str2[i + 1] * int(res2)
    
print(res2)