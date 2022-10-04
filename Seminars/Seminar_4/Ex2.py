# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя 
# способами:
    
#     1) с помощью математических формул нахождения корней 
#     квадратного уравнения
#     2) с помощью дополнительных библиотек Python
from math import sqrt
from unicodedata import digit

path = '/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_4/file3.txt'

file = open(path, 'r')

for line in file:
    print(line)
    list = line.split(' ')
    
    print(list)


resa = ''
for i in list[0]:
    
    if i.isdigit():
        resa += i
    else:
        break
print(resa)

resb = ''
for i in list[2]:
    
    if i.isdigit():
        resb += i
    else:
        break
print(resb)

a = int(resa)
b = int(resb)
c = int(list[4])

Dis = b ** 2 - 4 * a * c
print(Dis)

if list[1] == '-':
    b = -b
print(b)
if list[3] == '-':
    c = -c
print(c)

if Dis > 0:
    x1 = round((-b + sqrt(Dis)) / (2 * a), 2)
    x2 = round((-b - sqrt(Dis)) / (2 * a), 2)
    print(x1, x2)
elif Dis == 0:
    x = round(-b / (2 * a), 2)
    print(x)
else:
    print('Уравнение не имеет корней')



