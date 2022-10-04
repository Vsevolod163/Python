# Задайте строку из набора чисел. Напишите программу, которая 
# покажет большее и меньшее число. В качестве символа-разделителя 
# используйте пробел.

path = '/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_4/file1.txt'

file = open(path, 'r')

for line in file:
    if line != '\n':
        print(line)

list1 = []
res = ''
for i in line:
    if i != ' ':
        res += i
    else:
        list1.append(int(res))
        res = ''
min_index = 0
max_index = 0
for i in range(len(list1)):
    if list1[i] < list1[min_index]:
        min_index = i
    if list1[i] > list1[max_index]:
        max_index = i
print(list1[min_index], list1[max_index])
print(list1)

with open('/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_4/file2.txt', 'w') as data:
    data.write(str(list1[min_index]))
    data.write('\n')
    data.write(str(list1[max_index]))

file.close()

exit()


    
