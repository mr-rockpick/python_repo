# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
requested_vlan = input('Please, enter necessary vlan: ')

mac_table = []

with open('CAM_table.txt') as f:
    for line in f:
        values = line.split()
        if values and values[0].isdigit() and values[0] == requested_vlan:
            vlan, mac, _, port = values
            mac_table.append([int(vlan), mac, port])


for vlan, mac, port in sorted(mac_table):
    print(f'{vlan:<10}{mac:20}{port}')
