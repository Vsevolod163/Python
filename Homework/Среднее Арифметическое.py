# Среднее арифметическое из 4 чисел

l = int(input("Введите количество чисел: "))

sum = 0
for i in range(l):
    xi = int(input(f"Введите {i + 1} число: "))
    sum += xi

average = round(sum / l, 2)

print(average)