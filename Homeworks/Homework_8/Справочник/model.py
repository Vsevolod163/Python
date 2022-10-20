def open_file_list(path):
    with open(path) as file:
        list1 = ''
        for i in file:
            list1 += i
        res = list1.split('\n')
    return res

def open_file_string(path):

    string = ''
    with open(path) as file:
        for i in file:
            string += i
        return string

def remove_space(path, file):
    file3 = []
    for i in range(2, len(file)):
        if file[i] != '':
            file3.append(file[i])
        with open(path, 'w') as file2:
            file2.write('Лист контактов:\n')
        with open(path, 'a') as file2:
            for i in range(len(file3)):
                file2.write(f'\n{file3[i]}')
    return file3

def find_contact(contact, file):
    for i in file:
        if contact in i:
            print(i)

def add_contact(path, contact, file):
    file.append(contact)
    with open(path, 'w') as file2:
        file2.write('Лист контактов:\n')
    with open(path, 'a') as file2:
        for i in range(len(file)):
            file2.write(f'\n{file[i]}')

def del_contact(path, contact, file):
    for i in range(len(file)):
        if contact in file[i]:
            del file[i]
            break
    with open(path, 'w') as file2:
        file2.write('Лист контактов:\n')
    with open(path, 'a') as file2:
        for i in range(len(file)):
            file2.write(f'\n{file[i]}')

def change_contact(path, contact, file):
    for i in range(len(file)):
        if contact in file[i]:
            file[i] = str.title(input('Введите изменения: '))
            break
    with open(path, 'w') as file2:
        file2.write('Лист контактов:\n')
    with open(path, 'a') as file2:
        for i in range(len(file)):
            file2.write(f'\n{file[i]}')
    return file