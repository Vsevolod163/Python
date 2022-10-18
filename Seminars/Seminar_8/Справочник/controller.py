import model
import view

def button():
    path = '/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_8/Справочник/file.txt'
    res_file = model.open_file(path)
    
    do = view.what_to_do()
    if do == 'add':
        contact = view.input_contact()
        model.add_contact(path, contact, res_file)
        print(res_file)

    elif do == 'del':
        contact = view.input_contact()
        model.del_contact(path, contact, res_file)
        print(res_file)

    elif do == 'watch':
        print(res_file)