
from curses.ascii import isdigit
from re import A


a = '1 + 5 * 2 / 2'
# a = a.replace(' + ', ' +')
# a = a.replace(' - ', ' -')
print(a)
a = a.split()
print(a)

for i in range(len(a)):
    if a[i].isdigit():
        a[i] = int(a[i])
print(a)

for i in range(len(a)):
    if '*' in a or '/' in a:
        if a[i] == '*':
            a[i - 1] = a[i - 1] * a[i + 1]
            del a[i]
            print(i)
            
    print("1111")
        # del a[i:i + 1]
            # del a[i + 1]
    # elif '/' in a:
    #     if a[i] == '*':
    #         b = []
    #         if a[i] == '*':
    #             b.append(a[i - 1] * a[i + 1])
    #         del a[i - 1:i + 1]
            
# a.remove(a[i])
# a.remove(a[i + 1])
# print(f'!{a}')
            

            # a.remove([a[i - 1], a[i], a[i + 1]])
    # else:
    #     if a[i] == '+' or a[i] == '-':
    #         if a[i] == '+':
    #             b.append(a[i - 1] + a[i + 1])
    #         elif a[i] == '-':
    #             b.append(a[i - 1] - a[i + 1])

print(a)
# print(b)
# # print(a)
