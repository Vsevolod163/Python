from datetime import datetime as dt
from time import time

path1 = '/Users/seva/Desktop/Учеба/Python/Lections/Lection4/join_jon/log.csv'
def temperature_logger(data):
    with open(path1, 'a') as file:
        time = dt.now().strftime('%H:%M')
        file.write('{}; temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):
    with open(path1, 'a') as file:
        time = dt.now().strftime('%H:%M')
        file.write('{}; pressure;{}\n'
                    .format(time, data))

def wind_speed_logger(data):
    with open(path1, 'a') as file:
        time = dt.now().strftime('%H:%M')
        file.write('{}; wind_speed;{}\n'
                    .format(time, data))