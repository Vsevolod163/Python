# на вход приходит число и размер списка, вывести список первых элементов кратных числу

def county(x, size):
    result = []
    for i in range(0, size * x, x):
        result.append(x + i)
    return result
print(f'Через цикл: {county(3, 5)}')

# Через lambda and list comprehantions

print(f'Через lambda: {(lambda x, size: [x + i for i in range(0, size * x, x)])(3, 5)}')
