#!/usr/bin/env python

import random


life = []


def showList():
    nome = input("what's do you think about you? ")
    yes = input("yes or no")

    op = True
    while op:
        x = range(1, 5)
        op = input('put one world, do you like ')
        if yes == 'yes':
            break
        else:
            for item in op:
                print(item)
            if len(op) < 4:
                break
    else:

        print("my list favorite")


if __name__ == '__main__':
    showList()
