# Определить позицию второго вхождения строки в списке,
# либо сообщит, что ее нет

list1 = ['123', '124', 123, '127']

x = '123'

count = 0

for i in range(len(list1)):
    if list1[i] == x:
        count += 1

    if count == 2:
        print(i)
        break
else:
    if count == 0:

        print('Нет вхождения')
    else:
        print('Нет второго вхождения')



