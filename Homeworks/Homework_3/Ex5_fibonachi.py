# Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

def negafibonachi(n):

    list1 = [0, 0]
    list1[0] = 0
    list1[1] = 1

    list2 = []

    for i in range(2, n + 1):
        x = list1[i - 1] + list1[i - 2]     
        list1.append(x)
    
    l = len(list1) - 1

    for i in range(len(list1) - 1):

        if (l - i) % 2 == 0:
            j = - list1[l - i]
            list2.append(j)
        else:
            j = list1[l - i]
            list2.append(j)

    return list2 + list1

result = negafibonachi(8)

print(result)

