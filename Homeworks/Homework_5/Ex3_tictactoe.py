# Создайте программу для игры в 'Крестики-нолики'.

# ------------
#  1 | 2 | 3 |
# ------------
#  4 | 5 | 6 |
# ------------
#  7 | 8 | 9 |
# ------------ 

from curses.ascii import isdigit
import random

x = \
''' -----------
| 1 | 2 | 3 |
|-----------|
| 4 | 5 | 6 |
|-----------|
| 7 | 8 | 9 |
 -----------'''

res1 = ''

for i in x:
    if i.isdigit():
        res1 += i

x = list(x)

print(res1)

count = 0

check = random.randint(1, 2)

if check == 1:
    print('Первыми ходят X')
else:
    print('Первыми ходят O')

for i in range(1, 10):
    if i % 2 != 0:
        l = str(input('Введите номер четверти(1 - 9: '))
        while x[i].isdigit() == False and x[count] != l:
            count += 1
        else:
            if check == 1:
                x[count] = 'X'
                print(''.join(x))
                count = 0
            else:
                x[count] = '0'
                print(''.join(x))
                count = 0
    else:
        l = str(input('Введите номер четверти(1 - 9: '))
        while x[i].isdigit() == False and x[count] != l:
            count += 1
        else:
            if check == 1:
                x[count] = 'O'
                print(''.join(x))
                count = 0
            else:
                x[count] = 'X'
                print(''.join(x))
                count = 0
# print(x)


# k = '5 - 1 - 3 - 7'
# j = list(k)
# print(j)
# j = ''.join(j)
# print(j)
# g = k.replace('5', 'x')
# print(g)

# l = g.replace('1', 'x')
# print(l)