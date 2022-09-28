# Задайте список из n чисел последовательности (1+1/n)^n и выведите 
# на экран их сумму.

def list_of_numbers(N):

    array = []
    sum = 0

    for i in range(N):
        x = round(((1 + 1 / N) ** N), 2)
        array.append(x)
        sum += x

    print(array)

    return sum

result = round(list_of_numbers(5), 2)
print(f'Сумма элементов = {result}')