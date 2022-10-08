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
        print('\nПервыми ходит Игрок 1\n')
    else:
        print('\nПервыми ходит Игрок 2\n')

    list_check = ''

    print(''.join(x))

    for i in range(1, 10):
        if i % 2 != 0:
            l = str(input('Введите номер четверти(1 - 9): '))
            while l in list_check or int(l) < 1 or int(l) > 9:
                l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
            list_check += l

            while x[i].isdigit() == False and x[count] != l:
                count += 1
            else:
                x[count] = 'X'
                add_char(matrix_list, l, 'X')
                checkable = check_lines_cols(matrix_list)
                print(''.join(x))
                if checkable > 0:
                    if check == 1:
                        return(f'Stop! Выиграл Игрок 1!')
                    else:
                        return(f'Stop! Выиграл Игрок 2!')
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
                add_char(matrix_list, l, 'O')
                checkable = check_lines_cols(matrix_list)
                print(''.join(x))
                if checkable > 0:
                    if check == 1:
                        return(f'Stop! Выиграл Игрок 2!')
                    else: 
                        return(f'Stop! Выиграл Игрок 1!')
                count = 0
    
    return 'Ничья!'


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

    print(''.join(x))

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
                add_char(matrix_list, l, 'X')
                checkable = check_lines_cols(matrix_list)
                print(''.join(x))
                if checkable > 0:
                    return(f'Stop! Выиграл Бот {check}!')
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
                add_char(matrix_list, l, 'O')
                checkable = check_lines_cols(matrix_list)
                print(''.join(x))
                if checkable > 0:
                    return(f'Stop! Выиграл Бот {check2}!')
                count = 0
    
    return 'Ничья!'


# -----------------------------------------------Игрок против бота----------------------------------------------------------


def player_vs_bot(x):

    x = list(x)

    count = 0

    check = random.randint(1, 2)

    if check == 1:
        print('\nПервым ходит Игрок\n')
    else:
        print('\nПервым ходит Бот\n')

    list_check = ''

    print(''.join(x))

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
                    add_char(matrix_list, l, 'X')
                    checkable = check_lines_cols(matrix_list)
                    print(''.join(x))
                    if checkable > 0:
                        return(f'Stop! Выиграл Игрок!')
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
                    add_char(matrix_list, l, 'X')
                    checkable = check_lines_cols(matrix_list)
                    print(''.join(x))
                    if checkable > 0:
                        return(f'Stop! Выиграл Бот!')
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
                    add_char(matrix_list, l, 'O')
                    checkable = check_lines_cols(matrix_list)
                    print(''.join(x))
                    if checkable > 0:
                        return(f'Stop! Выиграл Бот!')
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
                    add_char(matrix_list, l, 'O')
                    checkable = check_lines_cols(matrix_list)
                    print(''.join(x))
                    if checkable > 0:
                        return(f'Stop! Выиграл Игрок!')
                    count = 0
                
    return 'Ничья!'

# -------------------------------------------------------------------------------------------------------------------------

def add_char(matrix_list, num, char):

    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            if matrix_list[i][j] == num:
                matrix_list[i][j] = char

    return matrix_list

def check_lines_cols(matrix_list):

    list_of_lines = []
    list_of_col = []

    for i in range(len(matrix_list)):
        list_of_lines.append(matrix_list[i])
        for j in range(len(matrix_list[i])):
            list_of_col.append(matrix_list[j][i])

    list_of_col_res = []
    for i in range(3, len(list_of_col) + 1, 3):
        list_of_col_res.append(list_of_col[i - 3:i])

    count = 0
   
    for i in list_of_lines:
        if len(set(i)) == 1:
            count += 1
            break

    for j in list_of_col_res:
        if len(set(j)) == 1:
            count += 1
            break
    
    if matrix_list[0][0] == matrix_list[1][1] == matrix_list[2][2] or matrix_list[0][2] == matrix_list[1][1] == matrix_list[2][0]:
        count += 1
    
    return count


x = \
''' -----------
| 1 | 2 | 3 |
|-----------|
| 4 | 5 | 6 |
|-----------|
| 7 | 8 | 9 |
 -----------'''

matrix_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


# game_of_two = two_players(x)
# print(game_of_two)

# game_of_bots = bot_vs_bot(x)
# print(game_of_bots)

game_player_vs_bot = player_vs_bot(x)
print(game_player_vs_bot)


