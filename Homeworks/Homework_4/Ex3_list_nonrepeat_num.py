# Задайте последовательность цифр. Напишите программу, которая 
# выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще 
# каким-нибудь способом кроме множества

# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random 

def list_uniq_el(N):
    
    count = 0

    list1 = []

    for i in range(len(N)):
        count = 0
        for j in range(len(N)):

            if j == i and N[i] == N[j]:
                count -= 1

            if N[i] == N[j]:
                count += 1 
        
        if count == 0:
            list1.append(int(N[i]))

    return list1

N = input('Введите последовательность: ')

x = list_uniq_el(N)

print(x)



# k = set()
# for i in range(10):
#     x = random.randint(1, 9)
#     print(x)
#     k.add(x)
    
# result = list(k)
# print(result)



