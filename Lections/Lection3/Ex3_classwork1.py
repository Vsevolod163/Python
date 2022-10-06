
path = '/Users/seva/Desktop/Учеба/Python/Lections/Lection3/classwork1'
with open(path) as file1:
    
    for i in file1:
        list1 = i.split(' ')
    
print(list1)

def f(x):
    x = int(x) ** 2
    return x
    
list2 = [(i, f(i)) for i in list1 if int(i) % 2 == 0]

print(list2)