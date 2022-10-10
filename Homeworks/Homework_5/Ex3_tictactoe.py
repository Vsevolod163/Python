# Создайте программу для игры в 'Крестики-нолики'.


from curses.ascii import isdigit
import random
import time


# ---------------------------------------------------2 игрока---------------------------------------------------------------


def two_players(x):

    x = list(x)
    count = 0
    check = random.randint(1, 2)

    if check == 1:
        print('\n' * 30  + ''.join(x2) + '\n' + 'Первым ходит Игрок 1\n' + '\n' * 30)
    else:
        print('\n' * 30 + ''.join(x2) + '\n' + 'Первым ходит Игрок 2\n' + '\n' * 30)

    list_check = []

    for i in range(1, size_of_matrix ** 2 + 1):
        if i % 2 != 0:
            l = str(input(f'Введите номер четверти(1 - {size_of_matrix ** 2}): '))
            while l in list_check or int(l) < 1 or int(l) > size_of_matrix ** 2:
                l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
            list_check.append(l)
            result = player1_win_check(add_char, check_lines_cols, i, check, 'X', l, x, x2, matrix_list, count, size_of_matrix)
            if result != None:
                return result
        else:
            l = str(input(f'Введите номер четверти(1 - {size_of_matrix ** 2}): '))
            while l in list_check or int(l) < 1 or int(l) > size_of_matrix ** 2:
                l = str(input('\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - 9): '))
            list_check.append(l)
            result = player2_win_check(add_char, check_lines_cols, i, check, 'O', l, x, x2, matrix_list, count, size_of_matrix)
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
        print('\n' * 30  + ''.join(x2) + '\n' + 'Первым ходит Бот 1\n' + '\n' * 30)
    else:
        check2 = 1
        print('\n' * 30  + ''.join(x2) + '\n' + 'Первым ходит Бот 2\n' + '\n' * 30)

    list_check = []

    for i in range(1, size_of_matrix ** 2 + 1):
        if i % 2 != 0:
            l = intelect_bot(matrix_list, 'X', 'O', size_of_matrix)
            if l != 0:
                list_check.append(str(l))
                result = bot_win_check(add_char, check_lines_cols, i, check, 'X', l, x, x2, matrix_list, count, size_of_matrix)
                if result != None:
                    return result
            else:
                l = str(random.randint(1, size_of_matrix ** 2))
                while l in list_check:
                    l = str(random.randint(1, size_of_matrix ** 2))
                list_check.append(l)
                result = bot_win_check(add_char, check_lines_cols, i, check, 'X', l, x, x2, matrix_list, count, size_of_matrix)
                if result != None:
                        return result
        else:
            l = intelect_bot(matrix_list, 'O', 'X', size_of_matrix)
            if l != 0:
                list_check.append(str(l))
                result = bot_win_check(add_char, check_lines_cols, i, check2, 'O', l, x, x2, matrix_list, count, size_of_matrix)
                if result != None:
                    return result
            else:
                l = str(random.randint(1, size_of_matrix ** 2))
                while l in list_check:
                    l = str(random.randint(1, size_of_matrix ** 2))
                list_check.append(l)
                result = bot_win_check(add_char, check_lines_cols, i, check2, 'O', l, x, x2, matrix_list, count, size_of_matrix)
                if result != None:
                    return result
    
    return 'Ничья!'


# -----------------------------------------------Игрок против бота----------------------------------------------------------


def player_vs_bot(x):

    x = list(x)
    count = 0
    check = random.randint(1, 2)
    if check == 1:
        print('\n' * 30  + ''.join(x2) + '\n' + 'Первым ходит Игрок\n' + '\n' * 30)
    else:
        print('\n' * 30 + ''.join(x2) + '\n' + 'Первым ходит Бот\n' + '\n' * 30)
    list_check = []
    for i in range(1, size_of_matrix ** 2 + 1):
        if i % 2 != 0: 
            if check == 1:
                l = str(input(f'Введите номер четверти(1 - {size_of_matrix ** 2}): '))
                while l in list_check or int(l) < 1 or int(l) > size_of_matrix ** 2:
                    l = str(input(f'\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - {size_of_matrix ** 2}): '))
                list_check.append(l)
                result = one_player_win_check(add_char, check_lines_cols, i, 'X', l, x, x2, matrix_list, count, size_of_matrix)
                if result != None:
                    return result
            else:
                if i == 1 and size_of_matrix ** 2 % 2 != 0:
                    l = str(int(size_of_matrix ** 2 / 2) + 1)
                    list_check.append(l)
                    one_bot_win_check(add_char, check_lines_cols, i, 'X', l, x, x2, matrix_list, count, size_of_matrix)
                else:
                    l = intelect_bot(matrix_list, 'X', 'O', size_of_matrix)
                    if l != 0:
                        list_check.append(str(l))
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'X', l, x, x2, matrix_list, count, size_of_matrix)
                        if result != None:
                            return result
                    else:
                        l = str(random.randint(1, size_of_matrix ** 2))
                        while l in list_check:
                            l = str(random.randint(1, size_of_matrix ** 2))
                        list_check.append(l)
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'X', l, x, x2, matrix_list, count, size_of_matrix)
                        if result != None:
                            return result
        else:
            if check == 1:
                if matrix_list[int(size_of_matrix / 2)][int(size_of_matrix / 2)].isdigit() and size_of_matrix ** 2 % 2 != 0:
                    l = l = str(int(size_of_matrix ** 2 / 2) + 1)
                    list_check.append(l)
                    one_bot_win_check(add_char, check_lines_cols, i, 'O', l, x, x2, matrix_list, count, size_of_matrix)
                else:    
                    l = intelect_bot(matrix_list, 'O', 'X', size_of_matrix)
                    if l != 0:
                        list_check.append(str(l))
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'O', l, x, x2, matrix_list, count, size_of_matrix)
                        if result != None:
                            return result
                    else:
                        l = str(random.randint(1, size_of_matrix ** 2))
                        while l in list_check:
                            l = str(random.randint(1, size_of_matrix ** 2))
                        list_check.append(l)
                        result = one_bot_win_check(add_char, check_lines_cols, i, 'O', l, x, x2, matrix_list, count, size_of_matrix)
                        if result != None:
                            return result
            else:
                l = str(input(f'Введите номер четверти(1 - {size_of_matrix ** 2}): '))
                while l in list_check or int(l) < 1 or int(l) > size_of_matrix ** 2:
                    l = str(input(f'\nЭта клетка уже занята или ее нет.\nВведите номер четверти(1 - {size_of_matrix ** 2}): '))
                list_check.append(l)
                result = one_player_win_check(add_char, check_lines_cols, i, 'O', l, x, x2, matrix_list, count, size_of_matrix)
                if result != None:
                    return result
                
    return 'Ничья!'


# ----------------------------------------------Функции для программ--------------------------------------------------------

def create_model_of_matrix(size_of_matrix):

    x4 = ' --- ' * size_of_matrix
    x5 = '|   |' * size_of_matrix
    x6 = ' --- ' * size_of_matrix

    x_res = (x4 + '\n' + x5 + '\n' + x6 + '\n') * size_of_matrix

    return x_res

def create_model_of_matrix_numbers(size_of_matrix):

    x5 = ''

    x4 = ' --- ' * size_of_matrix
    for i in range(size_of_matrix):
        x5 = x5 + f'| {str(i)} |'
        
    x6 = ' --- ' * size_of_matrix

    x_res = (x4 + '\n' + x5 + '\n' + x6 + '\n') * size_of_matrix

    count = 0
    count2 = 1

    x_res = list(x_res)

    for i in range(size_of_matrix ** 2):
        while x_res[count].isdigit() == False:
            count += 1
        else:
            x_res[count] = str(count2)
            count += 1
            count2 += 1

    return x_res

def create_list_of_lines(matrix_list):

    list_of_lines = []

    for i in range(len(matrix_list)):
        list_of_lines.append(matrix_list[i])

    return list_of_lines

def create_list_of_col(matrix_list, size):

    list_of_col = []

    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            list_of_col.append(matrix_list[j][i])

    list_of_col_res = []

    for i in range(size, len(list_of_col) + 1, size):
        list_of_col_res.append(list_of_col[i - size:i])

    return list_of_col_res

def create_matrix(size):

    new_matrix = []

    for i in range(size_of_matrix ** 2):
        new_matrix.append(str(i + 1))

    new_matrix_res = []

    for i in range(size, len(new_matrix) + 1, size):
            new_matrix_res.append(new_matrix[i - size:i])

    return new_matrix_res

def create_list_of_diag(matrix_list, size):

    list_of_diagonals = []

    for i in range(len(matrix_list)):
        list_of_diagonals.append(matrix_list[i][i])

    count = 1
    count2 = 0
    while count <= size and count2 <= size:   
        list_of_diagonals.append(matrix_list[count2][size_of_matrix - count])
        count += 1
        count2 += 1

    list_of_diagonals_res = []

    for i in range(size, len(list_of_diagonals) + 1, size):
        list_of_diagonals_res.append(list_of_diagonals[i - size:i])
  
    return list_of_diagonals_res

def intelect_bot(matrix_list, char, char2, size):

    list_of_lines = create_list_of_lines(matrix_list)
    list_of_col_res = create_list_of_col(matrix_list, size)
    list_of_diagonal_res = create_list_of_diag(matrix_list, size)
    
    temp = find_square(list_of_lines, char, size)
    if temp != None:
        return temp
    temp = find_square(list_of_col_res, char, size)
    if temp != None:
        return temp
    temp = find_square(list_of_diagonal_res, char, size)
    if temp != None:
        return temp
    temp = findsquare2(list_of_lines, char, char2, size)
    if temp != None:
        return temp
    temp = findsquare2(list_of_col_res, char, char2, size)
    if temp != None:
        return temp
    temp = findsquare2(list_of_diagonal_res, char, char2, size)
    if temp != None:
        return temp

    if temp == None:
        return 0

def player1_win_check(function1, function2, i, check, char, num, matrix, matrix2, matrix_list, count, size):

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        matrix2[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list, size)
        print('\n' * 30)
        print(''.join(matrix2))
        print(f'Ход Игрока: {num}')
        print('\n' * 30) 
        if checkable > 0:
            if check == 1:
                return(f'Stop! Выиграл Игрок 1!')
            else:
                return(f'Stop! Выиграл Игрок 2!')
        count = 0

def player2_win_check(function1, function2, i, check, char, num, matrix, matrix2, matrix_list, count, size):

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        matrix2[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list, size)
        print('\n' * 30)
        print(''.join(matrix2))
        print(f'Ход Игрока: {num}')
        print('\n' * 30)
        if checkable > 0:
            if check == 1:
                return(f'Stop! Выиграл Игрок 2!')
            else:
                return(f'Stop! Выиграл Игрок 1!')
        count = 0

def bot_win_check(function1, function2, i, check, char, num, matrix, matrix2, matrix_list, count, size):

    time.sleep(2)

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix2[count] = char
        matrix[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list, size)
        print('\n' * 30)
        print(''.join(matrix2))
        print(f'Ход Бота {check}: {num}')
        print('\n' * 30)
        if checkable > 0:
            return(f'Stop! Выиграл Бот {check}!')
        count = 0

def one_player_win_check(function1, function2, i, char, num, matrix, matrix2, matrix_list, count, size):

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        matrix2[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list, size)
        print('\n' * 30)
        print(''.join(matrix2))
        print(f'Ход Игрока: {num}')
        print('\n' * 30)
        if checkable > 0:
            return(f'Stop! Выиграл Игрок!')
        count = 0

def one_bot_win_check(function1, function2, i, char, num, matrix, matrix2, matrix_list, count, size):

    time.sleep(2)

    while matrix[i].isdigit() == False and matrix[count] != num:
        count += 1
    else:
        matrix[count] = char
        matrix2[count] = char
        function1(matrix_list, num, char)
        checkable = function2(matrix_list, size)
        print('\n' * 30)
        print(''.join(matrix2))
        print(f'Ход бота: {num}')
        print('\n' * 30)
        if checkable > 0:
            return(f'Stop! Выиграл Бот!')
        count = 0
   
def add_char(matrix_list, num, char):

    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            if matrix_list[i][j] == num:
                matrix_list[i][j] = char
    return matrix_list

def check_lines_cols(matrix_list, size):

    list_of_lines = create_list_of_lines(matrix_list)
    list_of_col_res = create_list_of_col(matrix_list, size)
    list_of_diagonal_res = create_list_of_diag(matrix_list, size)

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

def find_square(list, char, size):

    count = 1
    for i in range(len(list)):
        for j in range(len(list[i])):
            count = 1
            if len(set(list[i])) == 2 and char in list[i]:
                while count <= size:
                    if list[i][j] != list[i][size - count] and list[i][size - count].isdigit():
                        temp = list[i][size - count]
                        return temp
                    elif list[i][j] != list[i][size - count] and list[i][j].isdigit():
                        temp = list[i][j]
                        return temp
                    else:
                        count += 1
    else:
        count = 1
        for i in range(len(list)):
            for j in range(len(list[i])):
                count = 1
                if len(set(list[i])) == 2:
                    while count <= size:
                        if list[i][j] != list[i][size - count] and list[i][size - count].isdigit():
                            temp = list[i][size - count]
                            return temp
                        elif list[i][j] != list[i][size - count] and list[i][j].isdigit():
                            temp = list[i][j]
                            return temp
                        else:
                            count += 1

def findsquare2(list, char, char2, size):
    count = 1
    for i in range(len(list)):
        for count in range(1, len(list[i]) + 1):
            if len(set(list[i])) > 2 and char in list[i] and char2 not in list[i]:
                if list[i][size - count] != char and list[i][size - count].isdigit():
                    temp = list[i][size - count]
                    return temp
                   
                   

# -------------------------------------------------Входные элементы----------------------------------------------------------


size_of_matrix = int(input('Введите размер матрицы: '))
matrix_list = create_matrix(size_of_matrix)

x = create_model_of_matrix_numbers(size_of_matrix)

x2 = create_model_of_matrix(size_of_matrix)
x2 = list(x2)


# ----------------------------------------------------Вызов игр--------------------------------------------------------------


# game_of_two = two_players(x)
# print(game_of_two)

game_of_bots = bot_vs_bot(x)
print(game_of_bots)

# game_player_vs_bot = player_vs_bot(x)
# print(game_player_vs_bot)

