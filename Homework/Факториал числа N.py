# Факториал числа N

from re import I, X


l = int(input("Введите число: "))

fact = 1

for i in range(1, l + 1):
    fact *= i
    
    
print(fact)
