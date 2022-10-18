import model
import view

def button():
    print('''0. Показать все контакты
1. Открыть файл с контактами
2. Записать файл с контактами
3. Добавить контакт
4. Изменить контакт
5. Удалить контакт
6. Поиск по контактам''')
    path = '/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_8/Справочник/file.txt'
    res_file = model.open_file(path)
    
    do = view.what_to_do()
    if do == '3':
        contact = view.input_contact()
        model.add_contact(path, contact, res_file)
        print(res_file)

    elif do == '5':
        contact = view.input_contact()
        model.del_contact(path, contact, res_file)
        print(res_file)

    elif do == '0':
        print(res_file)