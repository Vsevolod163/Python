def input_value(string: str):
    try:
        value = int(input(string))
        return value
    except:
        print('Ошибка ввода')

def print_values(variable: int):
    print(variable)
