# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum(N):

    sum = 0

    for i in range(len(N)):

        if N[i] == ".":
            i += 1
        else:
            sum = sum + int(N[i])

    return sum

num = input("Введите число: ")
result = sum(num)
print(f"Сумма цифр в числе {num} = {result}")


