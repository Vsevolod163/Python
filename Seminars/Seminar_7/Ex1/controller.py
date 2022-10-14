
import model
import view
import log

def button_click():
    string_res = ''
    log.start_file()
    value_a = view.get_value()
    char = view.get_char()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it(char)
    string_res += f'{str(value_a)} {char} {str(value_b)} = {str(result)}'
    view.view_data(result)
    log.file_add(string_res)
    while char != '=':
        string_res = ''
        char = view.get_char()
        if char == '=':
            view.view_data(result)
            break
        value_b = view.get_value()
        model.init(result, value_b)
        temp = result
        result = model.do_it(char)
        view.view_data(result)
        string_res += f'{str(temp)} {char} {str(value_b)} = {str(result)}'
        log.file_add(string_res)

        

   