a = int(input('a = '))
b = int(input('b = '))

if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя: ')

if username == 'Маша':
    print('Ура, это Маша')
elif username == 'Ильнар':
    print('Привет, Ильнар')
    
else: 
    print(f'Привет, {username}')