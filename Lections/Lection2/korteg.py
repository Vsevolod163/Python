# кортеж - это неизменяемый список

a, b = 3, 4

a = (3, 4) # картеж
print(a)
print(a[0])

array = [1, 5, 7]
i = tuple(array) # перевод списка в картеж

print(i)

b = (3,) # если одно число, то после него ставить ,
print(b[0])

t = tuple(['red', 'green', 'blue'])
red, green, blue = t # распаковываем кортеж
print(red, green, blue)