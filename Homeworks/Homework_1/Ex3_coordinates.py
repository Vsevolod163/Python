# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).

# Пример:

# - x = 34; y = -30 -> 4
# - x = 2; y = 4-> 1
# - x = -34; y = -30 -> 3

def check_coordinates(x, y):
    
    while x == 0 or y == 0:
        print('x = 0 или y = 0, попробуйте снова:')
        x = int(input('Введите x: '))
        y = int(input('Введите y: '))
    else:
        if x < 0 and y > 0:
            return '1 четверть'
        elif x > 0 and y > 0:
            return '2 четверть'
        elif x < 0 and y < 0:
            return '3 четверть'
        elif x > 0 and y < 0:
            return '4 четверть'

x = int(input('Введите x: '))
y = int(input('Введите y: '))

print(check_coordinates(x, y))