for i in range(1, 6, 1):
    print(i)

count = 0
word = "Hello world!"
for i in word:
    if i == "!":
        count += 1

print("Count:", count)