i = 5

isHasCar = True

while isHasCar:
    if input("Enter data: ") == "Stop":
        isHasCar = False

for i in range(1, 11):
    if i == 5:
        break

    if i % 2 == 0:
        continue

    print(i)
