
from curses.ascii import isdigit

a = '4 + 5 * 2 / 2 - 4'
a = a.split()
for i in range(len(a)):
    if a[i].isdigit():
        a[i] = int(a[i])
print(a)
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
        if '+' in a or '-' in a:
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
print(a)

