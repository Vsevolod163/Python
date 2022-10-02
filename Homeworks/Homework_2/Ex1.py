# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# def sum(N):

#     sum = 0

    # for i in range(len(N)):

    #     if N[i] == ".":
    #         i += 1
    #     else:
#     for i in range(len(N)):
#         if N[i].isdigit(): # isdigit проверяет число ли это
#             sum = sum + int(N[i])

#     return sum

# num = input("Введите число: ")
# result = sum(num)
# print(f"Сумма цифр в числе {num} = {result}")

# num = abs(num) # abs - модуль

# while num != int(num):
#     num *= 10

# summa = 0

# while num > 0:
#     summa += num % 10
#     num //= 10

# print(summa)

def float_to_completed_integer(real_number):
    magnitude = 1
    temp = real_number
    while not temp.is_integer():
        magnitude *= 10
        temp = real_number * magnitude
        print(temp)
    return int(temp)


def get_digits_sum(any_number):
    no_point_number = float_to_completed_integer(any_number)
    no_point_number = abs(no_point_number)
    sum = 0
    while no_point_number > 0:
        sum += no_point_number % 10
        no_point_number //= 10
    return sum

print (get_digits_sum(0.57))