# Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

import time

def random1(n, min, max):

    list1 = []
    
    for i in range(1, n + 1):
        l = len(str(max))
        x = round(i * time.time() * 10 ** 10 % 10 ** l)
       
        while x > max or x < min:
            x = round(i * time.time() * 10 ** 10 % 10 ** l)
        
        if i % 2 == 0 and -x > min:
            list1.append(-x)
        else: 
            list1.append(x)   
    
    return list1

result_list = random1(9, -200, 500)
print(result_list)
