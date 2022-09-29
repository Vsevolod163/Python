colors = {'red', 'green', 'blue'}

colors.add('gray')

colors.remove('red')

colors.clear() # очищает множество

a = {1, 2, 3, 4, 5}
b = {2, 7, 8, 9, 0}

c = a.copy()

u = a.union(b) # объединение множеств

i = a.intersection(b) # выводит общие эл

dl = a.difference(b) # выводит эл, которых нет в множестве b

dr = b.difference(a)

s = frozenset(a) # замороженное(неизменяемое множество)
