# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# Ост от деления K (колич конфет) на m + 1 (колич конфет за один раз)

import random


# ------------------------------------------------------Бот против бота------------------------------------------------------


def bot_vs_bot(count_of_candies):

    first_move = random.randint(1, 2)
    if first_move == 1:
        second_move = 2
        print('Ходит Бот 1')
    else:
        second_move = 1
        print('Ходит Бот 2')

    count = 1

    while count_of_candies > 0:

        if count_of_candies <= 28 and count_of_candies > 0:
            bot_number = count_of_candies
            count_of_candies -= bot_number
            
            print(f'Ход Бота {first_move}: {bot_number}, Количество конфет: {count_of_candies}\nВыиграл Бот {first_move}!')
            
        else:
            if count % 2 != 0:
                bot_number = count_of_candies % (28 + 1)
                count_of_candies -= bot_number
                print(f'Ход Бота {first_move}: {bot_number}, Количество конфет: {count_of_candies}')
                count += 1

            else:
                bot_number = random.randint(1, 28)
                count_of_candies -= bot_number
                print(f'Ход Бота {second_move}: {bot_number}, Количество конфет: {count_of_candies}')
                count += 1


# ------------------------------------------------------Игрок против бота------------------------------------------------------


def player_vs_bot(count_of_candies):

    first_move = random.randint(1, 2)
    if first_move == 1:
        second_move = 2
        print('Ходит Игрок')
    else:
        second_move = 1
        print('Ходит Бот')

    count = 1

    while count_of_candies > 0:
        if count_of_candies <= 28:
            bot_number = count_of_candies
            count_of_candies -= bot_number
            if first_move == 1 and count % 2 != 0:
                print(f'Ход Игрока: {bot_number}, Количество конфет: {count_of_candies}\nВыиграл Игрок!')
            elif first_move == 1 and count % 2 == 0:
                print(f'Ход Бота: {bot_number}, Количество конфет: {count_of_candies}\nВыиграл Бот!')
            elif first_move == 2:
                print(f'Ход Бота: {bot_number}, Количество конфет: {count_of_candies}\nВыиграл Бот!')
            break
        else:
            if first_move == 1:
                if count % 2 != 0:
                    bot_number1 = count_of_candies % (28 + 1)
                    if count_of_candies % (28 + 1) != 0:
                        print(f'Советуем сходить {bot_number1}...')
                    bot_number = int(input('Сколько конфет Вы хотите взять(1-28)? '))
                    while bot_number < 1 or bot_number > 28:
                        bot_number = int(input('Введите количество от 1 до 28: '))
                    count_of_candies -= bot_number
                    print(f'Ход Игрока: {bot_number}, Количество конфет: {count_of_candies}')
                    count += 1
                else:
                    if count_of_candies % (28 + 1) != 0:
                        bot_number = count_of_candies % (28 + 1)
                        count_of_candies -= bot_number
                        print(f'Ход Бота {first_move}: {bot_number}, Количество конфет: {count_of_candies}')
                        count += 1
                    else:    
                        bot_number = random.randint(1, 28)
                        count_of_candies -= bot_number
                        print(f'Ход Бота {second_move}: {bot_number}, Количество конфет: {count_of_candies}')
                        count += 1
            else:
                if count % 2 != 0:
                    bot_number = count_of_candies % (28 + 1)
                    count_of_candies -= bot_number
                    print(f'Ход Бота {first_move}: {bot_number}, Количество конфет: {count_of_candies}')
                    count += 1
                else:
                    bot_number = int(input('Сколько конфет Вы хотите взять?(1 - 28) '))
                    while bot_number < 1 or bot_number > 28:
                        bot_number = int(input('Введите количество от 1 до 28: '))
                    count_of_candies -= bot_number
                    print(f'Ход Игрока: {bot_number}, Количество конфет: {count_of_candies}')
                    count += 1


count_of_candies = int(input('Введите количество конфет: '))

# game_bot_vs_bot = bot_vs_bot(count_of_candies)
game_player_vs_bot = player_vs_bot(count_of_candies)