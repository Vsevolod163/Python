data = input()

number = 5 if data == "Five" else 0 # Тернарный оператор, как if else, но в 1 строку
                                    # Используется, когда только if и else

if data == "Five":
    number = 5
else:
    number = 0

print(number)