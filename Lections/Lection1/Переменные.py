value = None
a = 5
b = 7.7
value = 12345

print(type(a))
print(type(b))
print(type(value))
s = 'hellow "world' # можно использовать двойные и одинарные ковычки
s = 'hello \' world'
s = 'hello \nworld'

print(s) # вывод строки
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)

