# На вход приходит число, вывести сумму элементов от 1 до данного числа

def summation(num):
    result = 0
    for i in range(1, num + 1):
        result += i
    return result

print(f'Через цикл: {summation(5)}')

res = lambda num: [i for i in range(num + 1)]
res2 = sum(list(res(5)))
print(f'Через lambda: {res2}')
# Перевод элементов списка в строку и обратно в int
res3 = list(map(str, res(5)))
res3 = sum(list(map(int, res(5))))
print(f'С использованием map: {res3}')
