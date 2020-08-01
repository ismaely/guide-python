#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# man.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   :
# @Date   : 01/08/2020, 14:33:19
import random


dis = []
for item in range(10):
    if item == 5:
        dis.append(item)
    else:
        for x in range(item):
            print(dis, '*', item)

