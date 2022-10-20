import model
import view

def button():
    print('''1. Показать все контакты
2. Добавить контакт
3. Изменить контакт
4. Удалить контакт
5. Поиск по контактам''')
    path = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_8/Справочник/file.txt'
    res_file = model.open_file_list(path)
    res_file = model.remove_space(path, res_file)
    do = view.what_to_do()
    if do == '1':
        res_string = model.open_file_string(path)
        view.print_result(res_string)
    elif do == '2':
        contact = view.input_contact()
        model.add_contact(path, contact, res_file)
    elif do == '3':
        contact = view.input_contact()
        model.change_contact(path, contact, res_file)
    elif do == '4':
        contact = view.input_contact()
        model.del_contact(path, contact, res_file)
    elif do == '5':
        contact = view.input_contact()
        model.find_contact(contact, res_file)