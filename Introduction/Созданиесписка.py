n = int(input("Enter length: "))

user_list = []

i = 0
while i < n:
    string = f"Enter element {i + 1}: "
    user_list.append(input(string))
    i += 1

print(user_list)