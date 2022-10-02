# Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def desyat_to_dvoich(n):

    result = ''

    while n > 0:

        x = n % 2

        result = str(x) + result

        n //= 2

    return result

desyat_chislo = int(input('Введите десятичное число: '))
result = desyat_to_dvoich(desyat_chislo)
print(result)