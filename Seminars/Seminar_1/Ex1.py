# Напишите программу, которая принимает на вход два 
# числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

def quadrat_chisla(x1, x2):
    if x1 == x2 ** 2 or x2 == x1 ** 2:
        return "Да, является"
    else: return "Нет, не является"
    

m = int(input("Введите первое число: "))
n = int(input("Введите второе число: "))

a = quadrat_chisla(m, n)
print(a)