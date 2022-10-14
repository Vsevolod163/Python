from datetime import datetime
from time import timezone

path = '/Users/seva/Desktop/Учеба/Python/Seminars/Seminar_7/Ex1/log.txt'

def file_add(num):
    now = datetime.now()
    with open(path, 'a') as file:
        file.write(f'{num}   time: {str(now)}\n')
        
def start_file():
    with open(path, 'w') as file:
        file.write(f'Start\n')