# Напишите программу, которая будет на вход принимать число 
# N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def numbers(m):

    list = []
    for i in range(-m, m + 1):
        list.append(i)

    return list

x = numbers(5)
print(x)

