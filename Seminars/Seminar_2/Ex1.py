# Напишите программу, которая принимает на вход число N и выдаёт 
# последовательность из N членов.
# Пример:
# o	Для N = 5: 1, -3, 9, -27, 81

def posled(N):

    array = []

    # num = 1
    for i in range(0, N + 1):
        array.append((-3) ** i)
        # num *= -3
    return array

array = posled(5)

print(array)