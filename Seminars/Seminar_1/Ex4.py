# Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3


# num = float(input("Введите число: "))

# number = int(num * 10 % 10)

# if num % 1 == 0:
#     print("Net")
# else:
#     print(number)

num = float(input("Введите число: "))

if float(num) == int(num):
    print("Целое")
else:
    print('Дробное')