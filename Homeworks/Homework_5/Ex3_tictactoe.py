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
            result = player1_win_check(add_char, check_lines_cols, i, check, 'X', l, x, matrix_list, count)
            if result != None:
                return result
        else:
            l = str(input('Введите номер четверти(1 - 9): '))
            while l in list_check or int(l) < 1 or int(l) > 9:
                l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
            list_check += l
            result = player2_win_check(add_char, check_lines_cols, i, check, 'O', l, x, matrix_list, count)
            if result != None:
                return result

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
            checkable = intelect_check_lines_cols_diag(matrix_list)
            if checkable > 0:
                l = intelect_bot(matrix_list, 'X')
                if l != 0:
                    list_check += str(l)
                    result = bot_win_check(add_char, check_lines_cols, i, check, 'X', l, x, matrix_list, count)
                    if result != None:
                        return result
                else:
                    l = str(random.randint(1, 9))
                    while l in list_check:
                        l = str(random.randint(1,9))
                    list_check += l
                    result = bot_win_check(add_char, check_lines_cols, i, check, 'X', l, x, matrix_list, count)
                    if result != None:
                        return result
            else:
                l = str(random.randint(1, 9))
                while l in list_check:
                    l = str(random.randint(1,9))
                list_check += l
                result = bot_win_check(add_char, check_lines_cols, i, check, 'X', l, x, matrix_list, count)
                if result != None:
                    return result
        else:
            checkable = intelect_check_lines_cols_diag(matrix_list)
            if checkable > 0:
                l = intelect_bot(matrix_list, 'O')
                if l != 0:
                    list_check += str(l)
                    result = bot_win_check(add_char, check_lines_cols, i, check2, 'O', l, x, matrix_list, count)
                    if result != None:
                        return result
                else:
                    l = str(random.randint(1, 9))
                    while l in list_check:
                        l = str(random.randint(1,9))
                    list_check += l
                    result = bot_win_check(add_char, check_lines_cols, i, check2, 'O', l, x, matrix_list, count)
                    if result != None:
                        return result
            else:
                l = str(random.randint(1, 9))
                while l in list_check:
                    l = str(random.randint(1,9))
                list_check += l
                result = bot_win_check(add_char, check_lines_cols, i, check2, 'O', l, x, matrix_list, count)
                if result != None:
                    return result
    
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
                result = one_player_win_check(add_char, check_lines_cols, i, 'X', l, x, matrix_list, count)
                if result != None:
                    return result
            else:
                checkable = intelect_check_lines_cols_diag(matrix_list)
                if checkable > 0:
                    l = intelect_bot(matrix_list, 'X')
                    if l != 0:
                        list_check += str(l)
                        print(f'Ход бота: {l}')
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'X', l, x, matrix_list, count)
                        if result != None:
                            return result
                    else:
                        l = str(random.randint(1, 9))
                        while l in list_check:
                            l = str(random.randint(1,9))
                        list_check += l
                        print(f'Ход бота: {l}')
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'X', l, x, matrix_list, count)
                        if result != None:
                            return result
                else:
                    l = str(random.randint(1, 9))
                    while l in list_check:
                        l = str(random.randint(1,9))
                    list_check += l
                    print(f'Ход бота: {l}')
                    result = one_bot_win_check(add_char, check_lines_cols, i, 'X', l, x, matrix_list, count)
                    if result != None:
                        return result
        else:
            if check == 1:
                checkable = intelect_check_lines_cols_diag(matrix_list)
                if checkable > 0:
                    l = intelect_bot(matrix_list, 'O')
                    if l != 0:
                        list_check += str(l)
                        print(f'Ход бота: {l}')
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'O', l, x, matrix_list, count)
                        if result != None:
                            return result
                    else:
                        l = str(random.randint(1, 9))
                        while l in list_check:
                            l = str(random.randint(1,9))
                        list_check += l
                        print(f'Ход бота: {l}')
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'O', l, x, matrix_list, count)
                        if result != None:
                            return result
                else:        
                    l = str(random.randint(1, 9))
                    while l in list_check:
                        l = str(random.randint(1,9))
                    list_check += l
                    print(f'Ход бота: {l}')
                    result = one_bot_win_check(add_char, check_lines_cols, i, 'O', l, x, matrix_list, count)
                    if result != None:
                        return result
            else:
                l = str(input('Введите номер четверти(1 - 9): '))
                while l in list_check or int(l) < 1 or int(l) > 9:
                    l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
                list_check += l
                result = one_player_win_check(add_char, check_lines_cols, i, 'O', l, x, matrix_list, count)
                if result != None:
                    return result
                
    return 'Ничья!'


# ----------------------------------------------Функции для программ--------------------------------------------------------


def create_list_of_lines(matrix_list):

    list_of_lines = []

    for i in range(len(matrix_list)):
        list_of_lines.append(matrix_list[i])

    return list_of_lines

def create_list_of_col(matrix_list):

    list_of_col = []

    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            list_of_col.append(matrix_list[j][i])

    list_of_col_res = []

    for i in range(3, len(list_of_col) + 1, 3):
        list_of_col_res.append(list_of_col[i - 3:i])

    return list_of_col_res

def create_list_of_diag(matrix_list):

    list_of_diagonal = []
    list_of_diagonal_res = []

    list_of_diagonal.append(matrix_list[0][0])
    list_of_diagonal.append(matrix_list[1][1])
    list_of_diagonal.append(matrix_list[2][2])
    list_of_diagonal.append(matrix_list[0][2])
    list_of_diagonal.append(matrix_list[1][1])
    list_of_diagonal.append(matrix_list[2][0])

    list_of_diagonal_res.append(list_of_diagonal[:3])
    list_of_diagonal_res.append(list_of_diagonal[3:6])

    return list_of_diagonal_res

def intelect_bot(matrix_list, char):

    list_of_lines = create_list_of_lines(matrix_list)
    list_of_col_res = create_list_of_col(matrix_list)
    list_of_diagonal_res = create_list_of_diag(matrix_list)
    
    temp = find_square(list_of_lines, char)
    if temp != None:
        return temp
    temp = find_square(list_of_col_res, char)
    if temp != None:
        return temp
    temp = find_square(list_of_diagonal_res, char)
    if temp != None:
        return temp

    if temp == None:
        return 0

def player1_win_check(function1, function2, i, check, char, num, matrix, matrix_list, count):

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list)
        print(''.join(matrix))
        if checkable > 0:
            if check == 1:
                return(f'Stop! Выиграл Игрок 1!')
            else:
                return(f'Stop! Выиграл Игрок 2!')
        count = 0

def player2_win_check(function1, function2, i, check, char, num, matrix, matrix_list, count):

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list)
        print(''.join(matrix))
        if checkable > 0:
            if check == 1:
                return(f'Stop! Выиграл Игрок 2!')
            else:
                return(f'Stop! Выиграл Игрок 1!')
        count = 0

def bot_win_check(function1, function2, i, check, char, num, matrix, matrix_list, count):

    print(f'Ход Бота {check}: {num}')
    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list)
        print(''.join(matrix))
        if checkable > 0:
            return(f'Stop! Выиграл Бот {check}!')
        count = 0

def one_player_win_check(function1, function2, i, char, num, matrix, matrix_list, count):

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list)
        print(''.join(matrix))
        if checkable > 0:
            return(f'Stop! Выиграл Игрок!')
        count = 0

def one_bot_win_check(function1, function2, i, char, num, matrix, matrix_list, count):

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list)
        print(''.join(matrix))
        if checkable > 0:
            return(f'Stop! Выиграл Бот!')
        count = 0

def intelect_check_lines_cols_diag(matrix_list):

    list_of_lines = create_list_of_lines(matrix_list)
    list_of_col_res = create_list_of_col(matrix_list)
    list_of_diagonal_res = create_list_of_diag(matrix_list)
    
    count = 0
   
    for i in list_of_lines:
        if len(set(i)) == 2:
            count += 1
            break

    for j in list_of_col_res:
        if len(set(j)) == 2:
            count += 1
            break
    
    for k in list_of_diagonal_res:
        if len(set(k)) == 2:
            count += 1
            break     

    return count
   
def add_char(matrix_list, num, char):

    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            if matrix_list[i][j] == num:
                matrix_list[i][j] = char

    return matrix_list

def check_lines_cols(matrix_list):

    list_of_lines = create_list_of_lines(matrix_list)
    list_of_col_res = create_list_of_col(matrix_list)
    list_of_diagonal_res = create_list_of_diag(matrix_list)

    count = 0
   
    for i in list_of_lines:
        if len(set(i)) == 1:
            count += 1
            break

    for j in list_of_col_res:
        if len(set(j)) == 1:
            count += 1
            break
    
    for k in list_of_diagonal_res:
        if len(set(k)) == 1:
            count += 1
            break    
    
    return count

def find_square(list, char):

    for i in range(len(list)):
        if len(set(list[i])) == 2 and char in list[i]:
            if list[i][0] == list[i][1]:
                if list[i][2].isdigit():
                    temp = list[i][2]
                    return temp
            elif list[i][0] == list[i][2]:
                if list[i][1].isdigit():
                    temp = list[i][1]
                    return temp
            elif list[i][1] == list[i][2]:
                if list[i][0].isdigit():
                    temp = list[i][0]
                    return temp
    else:
        for i in range(len(list)):
            if len(set(list[i])) == 2:
                if list[i][0] == list[i][1]:
                    if list[i][2].isdigit():
                        temp = list[i][2]
                        return temp
                elif list[i][0] == list[i][2]:
                    if list[i][1].isdigit():
                        temp = list[i][1]
                        return temp
                elif list[i][1] == list[i][2]:
                    if list[i][0].isdigit():
                        temp = list[i][0]
                        return temp

# -------------------------------------------------Входные элементы----------------------------------------------------------


x = \
''' -----------
| 1 | 2 | 3 |
|-----------|
| 4 | 5 | 6 |
|-----------|
| 7 | 8 | 9 |
 -----------'''


matrix_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


# ----------------------------------------------------Вызов игр--------------------------------------------------------------


# game_of_two = two_players(x)
# print(game_of_two)

game_of_bots = bot_vs_bot(x)
print(game_of_bots)

# game_player_vs_bot = player_vs_bot(x)
# print(game_player_vs_bot)
