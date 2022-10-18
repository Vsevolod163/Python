def open_file(path):
    with open(path) as file:
        list1 = ''
        for i in file:
            list1 += i
        res = list1.split('\n')
        print(res)
    return res

def add_contact(path, contact, file):
    file.append(contact)
    with open(path, 'a') as file1:
        file1.write(f'\n{contact}')


def del_contact(path, contact, file):
    for i in range(len(file)):
        if contact in file[i]:
            del file[i]
            break
    with open(path, 'w') as file2:
        file2.write('Лист контактов')
    with open(path, 'a') as file2:
        for i in range(1, len(file)):
            file2.write(f'\n{file[i]}')