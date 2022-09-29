from turtle import up


dictionary = {} # создание словаря

# \ - чтобы не писать в одну строчку

dictionary = \
    {
        'up': '1', # up - ключ
        'left': '2',
        'down': '3',
        'right': '4'
    }

print(dictionary)
print(dictionary['left'])

for k in dictionary.keys(): # показывает только ключи
    print(k)

for v in dictionary.values(): # показывает только значения
    print(v)

dictionary['up'] = 'up1' # в словаре можно менять значения эл
print(dictionary['up'])

del dictionary['right']

for i in dictionary: # вывод всего словаря (i - это ключ)

    print(f'{i}: {dictionary[i]}')