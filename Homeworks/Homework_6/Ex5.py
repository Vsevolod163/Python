# Вывсти только четные элементы списка

import random

list1 = [random.randint(-10, 10) for _ in range(5)]
print(list1)

print(list(filter(lambda x: x % 2 == 0, list1)))