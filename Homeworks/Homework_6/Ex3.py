# На вход приходит число, вывести сумму элементов от 1 до данного числа

def summation(num):
    result = 0
    for i in range(1, num + 1):
        result += i
    return result

print(f'Через цикл: {summation(5)}')

res = (lambda num: [i for i in range(1, num + 1)])(5)
print(f'Список элементов: {list(res)}')
print(f'Через lambda: {sum(res)}')
# Перевод элементов списка в строку и обратно в int
res2 = list(map(str, res))
print(f'Перевод элементов в str: {res2}')
res2 = sum(list(map(int, res)))
print(f'С использованием map: {res2}')
