import random

def create_random_list(n):

    list1 = []

    for i in range(n):
        x = round(random.randint(-9, 9) * random.random(), 2)
        list1.append(x)

    return list1
