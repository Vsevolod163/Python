# Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".

def open_file(path):
    with open(path) as file:
        res = ''
        for line in file:
            res += line
    
    return res

def write_file(path, x):
    with open(path, 'w') as file:
        file.write(str(x))

def delete_keywords(string, keyword):
    list = string.split(' ')
    list2 = []
    for i in range(len(list)):
        if not keyword in list[i]:
            list2.append(list[i]) 
    return list2

path = '/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_5/file1'
path2 = '/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_5/file2'
text = open_file(path)
word = 'ля'

list1 = delete_keywords(text, word)
print(list1)
list1 = ' '.join(list1)
result = write_file(path2, list1)
 