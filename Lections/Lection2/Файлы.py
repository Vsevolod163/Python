# 1 вариант

# colors = ['red', 'green', 'blue']
# data = open('Lection_2.txt', 'a')
# data.writelines(colors)
# data.write('\nLine 1\n')
# data.write('Line 2')

# data.close()

# 2 вариант

# with open('Lection_2.txt', 'a') as data:
#     data.write('\nLine 3\n')
#     data.write('Line 4')

# 3 вариант

path = 'Lection_2.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()