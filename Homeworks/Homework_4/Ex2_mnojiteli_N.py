# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

def list_of_mnoj(N):

    i = 2
    count = 0

    list_prost_mnoj = []
    while N <= 0 or N == 1:
        N = int(input('Введите натуральное число отличное от 1: '))

    while N != 1:
        
        if N % i == 0:

            N /= i
            list_prost_mnoj.append(i)
            count += 1

        else:

            i += 1

    if count == 1:
        return 'Число простое'
    else:
        return list_prost_mnoj

N = int(input('Введите натуральное число отличное от 1: '))

result = list_of_mnoj(N)

print(f'Результат: {result}')


