#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
file = argv[1]
newfile = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(file) as f, open(newfile, 'w') as fnew:
    for line in f:
        if line.startswith('!'):
            pass
        elif ignore[0] in line:
            pass
        elif ignore[1] in line:
            pass
        elif ignore[2] in line:
            pass
        else:
            fnew.write(line)
