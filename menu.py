#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# menu.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   :
# @Date   : 01/08/2020, 02:41:55

loop = 1
while (loop < 3):
    nome = input(" whats is your name: ")
    fone = input(" whats is your fone number: ")
    leads = input(" do you is leads: ")

    if leads == 'yes':
        break

    print("nome: %s" % nome)
    print("fone: %s" % fone)
    print("leads: %s" % leads)
    loop = loop + 1
