from datetime import datetime

path = '/Users/seva/Desktop/Учеба/Python/Homeworks/Homework_7/log.txt'
now = datetime.now()
def add_to_file(result, temp):
    with open(path, 'a') as file:
        file.write(f'Результат уравнения: {temp} = {result}   {str(now)}\n')