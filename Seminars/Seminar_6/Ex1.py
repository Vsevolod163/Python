# Ввести с клавиатуры 2 числа (int) и вывести в консоль их НОК 
# (наименьшее общее кратное)

from re import A


x1 = int(input('Введите число 1: '))
x2 = int(input('Введите число 2: '))

x3 = max(x1, x2)

res = 0
i = 1
a = 0

for i in range(1, x1 * x2 + 1):
    if i % x1 == 0 and i % x2 == 0:
        
        print(i)
        break
