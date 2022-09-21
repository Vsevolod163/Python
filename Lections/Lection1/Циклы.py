original = 23
inverted = 0

while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Хватит')
print(inverted)


for i in 1, 2, 3, 4, 5:
    print(i ** 2)

list = [1, 2, 3, 4]
for i in list:
    print(i)


for i in range(1, 10, 2): # (первое число, последнее число - 1, на сколько увеличивать)
    print(i)

for i in 'qwe':
    print(i)

text = 'съешь еще этих мягких французских булок'
print(len(text)) #39
print('еще' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('еще', 'ЕЩЕ')) 

for c in text:
    print(c)

# help(text.istitle) # описание функции

print(text[-5]) # покажет 5 й символ с конца
print(text[:]) # [0 эл : крайний эл]

numbers = [1, 5, 4]

numbers.append(10) # добавляет эл
numbers.remove(1) # убирает эл
print(numbers)