# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_numbers(x, y, z):

    y1 = not(x or y or z)
    y2 = not x and not y and not z
    if y1 == y2:
        return True 
    else:
        return False


X = int(input('Введите X: '))
Y = int(input('Введите Y: '))
Z = int(input('Введите Z: '))

print(check_numbers(X, Y, Z))