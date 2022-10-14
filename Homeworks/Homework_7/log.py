path = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_7/log.txt'

def add_to_file(result, temp):
    with open(path, 'w') as file:
        file.write(f'Результат уравнения: {temp} = {result}')