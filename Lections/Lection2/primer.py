def concatenatio(*params): # * перед переменной = сколько угодно элементов
    res: str = ''
    for item in params:
        res += item

    return res

print(concatenatio('a', 's', 'd'))