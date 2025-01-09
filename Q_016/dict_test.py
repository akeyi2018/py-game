from player_data import *

status_list = {
            "name": NAME,
            "job": JOB,
            "HP": HP,
            "MP": MP,
            "LV": LV
        }

y = [
    10, 20, 30, 40, 50
]

for (k,v), y in zip(status_list.items(), y):
    print(f'k:{k} v:{v} y:{y}')

