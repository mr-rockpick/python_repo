# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip = input('please, enter your ip address like this 10.0.1.1: ')
    ip_edit = ip.split('.')
    valid_ip = len(ip_edit) == 4

    for ip in ip_edit:
        valid_ip = ip.isdigit() and int(ip) in range(256) and valid_ip

    if valid_ip == False:
        print('incorrect ip')
    else:
        break


if 1 <= int(ip_edit[0]) <= 223:
    print('unicast')
elif 224 <= int(ip_edit[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
