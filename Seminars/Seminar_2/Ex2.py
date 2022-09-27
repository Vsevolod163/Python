# list = []

# list.append(3)
# dict = {}
# dict[1] = 'Вова'
# dict[78] = 'Игорь'

# print(list)
# print(dict)
# print(dict.get(3))

# Для натурального n создать словарь индекс-значение, состоящий 
# из элементов последовательности 3n + 1.
# Пример:
# o	Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

dict = {}

N = 6

for i in range(1, N + 1):
    dict[i] = 3 * i + 1

print(dict)

def new_array(l):
    array = []
    for i in range(l):
        x = int(input(f"Введите {i + 1} элемент: "))
        array.append(x)

    return array

array = new_array(5)
print(array)