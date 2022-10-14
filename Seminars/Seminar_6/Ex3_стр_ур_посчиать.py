
from curses.ascii import isdigit

b = '-  20 - 2 * 1 / 2'
b = b.replace(' ', '')
a = []
i = 0
while i < len(b):
    res = ''
    if i == 0 and b[i] == '-':
        res += b[i]
        i += 1
    while b[i].isdigit():
        if i == len(b) - 1:
           res += b[i]
           i += 1
           a.append(int(res))
           break
        else:
            res += b[i]
            i += 1
    else:
        a.append(int(res))
        a.append(b[i])
        i += 1
temp = ' '.join(map(str, a))
for _ in range(len(a)):
    for i in range(len(a)):
        if '*' in a or '/' in a:
            if a[i] == '*':
                a[i - 1] = a[i - 1] * a[i + 1]
                del a[i:i+2]
                break
            else:
                if a[i] == '/':
                    a[i - 1] = a[i - 1] / a[i + 1]
                    del a[i:i+2]
                    break
        elif '+' in a or '-' in a:
            if a[i] == '+':
                a[i - 1] = a[i - 1] + a[i + 1]
                del a[i:i+2]
                break
            else:
                if a[i] == '-':
                    a[i - 1] = a[i - 1] - a[i + 1]
                    del a[i:i+2]
                    break

a = ''.join(map(str, a))
print(f'Результат уравнения: {temp} = {a}')

