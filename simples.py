#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# simples.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   :
# @Date   : 01/08/2020, 02:12:15

aux = []
header = ''
fruits = ['apple', 'banana', 'cherry', 'uva',
          'manga', 'laranja', 'abacate', 'folha', 'tomate']
for x in fruits:
    print('--')
    if x != 'banana':
        aux.append(x)
        # print(aux)
    header = x

print('header -> %s' % header)
