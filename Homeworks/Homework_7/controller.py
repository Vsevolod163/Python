
import model
import view

def button_click():
    string = view.input_string()
    model.init(string)
    string = model.string_to_list(string)
    temp = ' '.join(map(str, string))
    result = model.result(string)
    result = model.list_to_string(string)
    view.print_result(result, temp)