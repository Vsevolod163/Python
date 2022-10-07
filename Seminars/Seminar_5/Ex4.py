# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие 
# A[i] - 1 = A[i-1]. Найдите это число.

# 1 2 3 4 5 6 7 8 => 4

str1 = '1 2 3 5 6 7 8 9'

list1 = str1.split()
print(list1)

def find_number(list1):

    x = 0
    for i in range(len(list1)):
        if int(list1[i]) - 1 != int(list1[i - 1]):
            x = int(list1[i]) - 1
            
    return x

x = find_number(list1)
print(x)