# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
network_template = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''

mask_template = '''
Mask:
/{mask}
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
ip = input('Please, enter a network address in a format like this 10.1.1.0/24: ')
ip_list = ip.split('/')
#print(ip_list)


network = ip_list[0]
#print(network)
x = network.replace('.', ' ')
y = x.split()
a = y[0]
aa = int(a)
b = y[1]
bb = int(b)
c = y[2]
cc = int(c)
d = y[3]
dd = int(d)


mask1 = int(ip_list[1])
#print(mask1)
mask2 = int(mask1)
mask = '1' * mask2 + '0' * (32 - mask2)
#print(mask)
i1 = mask[0:8]
i2 = mask[8:16]
i3 = mask[16:24]
i4 = mask[24:32]
#print(i1, i2, i3, i4)
j1 = int(i1, 2)
j2 = int(i2, 2)
j3 = int(i3, 2)
j4 = int(i4, 2)
#print(j1, j2, j3, j4)

print(network_template.format(aa, bb, cc, dd) + mask_template.format(j1, j2, j3, j4, mask=mask1))
#print(mask_template.format(j1, j2, j3, j4, mask=mask1))
