# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 10)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень 
# следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 
# просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random 

def func(k):

    res = ''
    list1 = ['-', '+']

    while k >= 0:
        a = random.randint(0, 10)
        if a == 0 and k == 0:
            res += ' = 0'
            break
        elif a == 0:
            k -= 1
        elif k == 1:
            if a == 1:
                res += f' {random.choice(list1)} x'
                k -= 1
            else:    
                res += f' {random.choice(list1)} {a}x'
                k -= 1
        elif k == 0:
            res += f' {random.choice(list1)} {a} = 0'
            break
        else:
            if a == 1:
                res += f' {random.choice(list1)} x^{k}'
                k -= 1
            else:    
                res += f' {random.choice(list1)} {a}x^{k}'
                k -= 1

    res = res[3:len(res)]
    
    return res

k = int(input('Введите натуральную степень k: '))
result = func(k)

print(result)

path = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_4/Ex4_file'

with open(path, 'w') as file:
    file.write(result)

    
    
