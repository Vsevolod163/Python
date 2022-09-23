# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def check_quater_number(x):
    
    while x < 1 or x > 4:
        print('Ошибка, попробуйте еще раз:')
        x = int(input('Введите номер четверти: '))
    else:
        if x == 1:
            return 'x < 0; y > 0'
        elif x == 2:
            return 'x > 0; y > 0'
        elif x == 3:
            return 'x < 0; y < 0'
        elif x == 4:
            return 'x > 0; y < 0'

x = int(input('Введите номер четверти: '))
checkable = check_quater_number(x)

print(checkable)
