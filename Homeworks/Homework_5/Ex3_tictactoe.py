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


# ---------------------------------------------------2 игрока---------------------------------------------------------------


def two_players(x):

    x = list(x)

    count = 0

    check = random.randint(1, 2)

    if check == 1:
        print('Первыми ходят X')
    else:
        print('Первыми ходят O')

    list_check = ''

    for i in range(1, 10):
        if i % 2 != 0:
            l = str(input('Введите номер четверти(1 - 9): '))
            while l in list_check or int(l) < 1 or int(l) > 9:
                l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
            list_check += l

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
            l = str(input('Введите номер четверти(1 - 9): '))
            while l in list_check or int(l) < 1 or int(l) > 9:
                l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
            list_check += l

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

    return 'Конец!'


# ------------------------------------------------Бот против бота-----------------------------------------------------------


def bot_vs_bot(x):

    x = list(x)

    count = 0

    check = random.randint(1, 2)

    if check == 1:
        check2 = 2
        print('\nПервым ходит бот 1\n')
    else:
        check2 = 1
        print('\nПервым ходит бот 2\n')

    list_check = ''
    for i in range(1, 10):
        if i % 2 != 0:
            l = str(random.randint(1, 9))
            while l in list_check:
                l = str(random.randint(1,9))
            list_check += l
            print(f'Ход бота {check}: {l}')
            while x[i].isdigit() == False and x[count] != l:
                count += 1
            else:
                x[count] = 'X'
                print(''.join(x))
                count = 0
               
        else:
            l = str(random.randint(1, 9))
            while l in list_check:
                l = str(random.randint(1,9))
            list_check += l
            print(f'Ход бота {check2}: {l}')
            while x[i].isdigit() == False and x[count] != l:
                count += 1
            else:
                x[count] = 'O'
                print(''.join(x))
                count = 0
    
    return 'Конец!'


# -----------------------------------------------Игрок против бота----------------------------------------------------------



def player_vs_bot(x):

    x = list(x)

    count = 0

    check = random.randint(1, 2)

    if check == 1:
        print('Первым ходит игрок')
    else:
        print('Первым ходит Бот')

    list_check = ''

    for i in range(1, 10):
        if i % 2 != 0: 
            if check == 1:
                l = str(input('Введите номер четверти(1 - 9): '))
                while l in list_check or int(l) < 1 or int(l) > 9:
                    l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
                list_check += l

                while x[i].isdigit() == False and x[count] != l:
                    count += 1
                else:
                    x[count] = 'X'
                    print(''.join(x))
                    count = 0
            else:
                l = str(random.randint(1, 9))
                while l in list_check:
                    l = str(random.randint(1,9))
                list_check += l
                print(f'Ход бота: {l}')
                while x[i].isdigit() == False and x[count] != l:
                    count += 1
                else:
                    x[count] = 'X'
                    print(''.join(x))
                    count = 0

        else:
            if check == 1:
                l = str(random.randint(1, 9))
                while l in list_check:
                    l = str(random.randint(1,9))
                list_check += l
                print(f'Ход бота: {l}')
                while x[i].isdigit() == False and x[count] != l:
                    count += 1
                else:
                    x[count] = 'O'
                    print(''.join(x))
                    count = 0
                
            else:
                l = str(input('Введите номер четверти(1 - 9): '))
                while l in list_check or int(l) < 1 or int(l) > 9:
                    l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
                list_check += l

                while x[i].isdigit() == False and x[count] != l:
                    count += 1
                else:
                    x[count] = 'O'
                    print(''.join(x))
                    count = 0
                
    return 'Конец!'


x = \
''' -----------
| 1 | 2 | 3 |
|-----------|
| 4 | 5 | 6 |
|-----------|
| 7 | 8 | 9 |
 -----------'''

game_of_two = two_players(x)
print(game_of_two)

# game_of_bots = bot_vs_bot(x)
# print(game_of_bots)

# game_player_vs_bot = player_vs_bot(x)
# print(game_player_vs_bot)

