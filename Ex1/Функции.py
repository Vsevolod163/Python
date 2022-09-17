numbers = [5, 2, 7]

# numbers[3] = 100

numbers.append(100) # Добавляет элемент в конец массива 
numbers.insert(1, True) # Добавляет элемент в нужное место массива

numbers.extend([5, 6, 8])
numbers.sort() # Сортировка от минимального к максимальному
# numbers.reverse() # Переворот массива
print(numbers)

numbers.pop() # Удаляет последний элемент
numbers.pop(1) # Удаляет элемент по индексу
numbers.remove(7) # Удаляет определенный элемент массива (само значение)
# numbers.clear() # Очищает массив
x = numbers.count(5) # Считает сколько элементов с данным значением в массиве
print(x)
print(len(numbers))
print(numbers)