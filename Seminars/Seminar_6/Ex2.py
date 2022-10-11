import random

myList1 = [random.randint(-100, 100) for _ in range(10)]
myList2 = [random.randint(-100, 100) for _ in range(10)]
myList3 = [random.randint(-100, 100) for _ in range(10)]
 # _ чтобы не задавать значение i в цикле

# myList = list(map(str, myList))
# print(myList)

myList = list(map(lambda x:x + 1, myList1))
print(myList1)

asasf = list(enumerate(myList1))
print(asasf)

for i in enumerate(myList1):
    if i[1] > 40:
        print(i[0])

myList = list(zip(myList1, myList2, myList3))
print(myList)