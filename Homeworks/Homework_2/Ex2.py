# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multi_of_numbers(N):

    multi = []
    x = 1

    for i in range(1, N + 1):

        x = x * i
        multi.append(x)

    return multi


num = int(input("Введите число: "))
result = multi_of_numbers(num)
print(f'Набор произведений чисел от 1 до {num} = {result}')