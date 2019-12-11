#!/usr/bin/env python3
# coding: utf-8
import numpy as np


def masstofuel(mass):
    return np.floor(mass/3) - 2


def enigma1(g):
    count = 0
    for sc in g:
        i = int(sc)
        count += masstofuel(i)
    return count


def enigma2(g, debug=False):
    count = 0
    for sc in g:
        i = int(sc)
        checker = i
        inner_summ = 0
        while checker > 3:
            checker = masstofuel(checker)
            if checker > 0:
                inner_summ += checker
            if debug:
                print("Checker:" + str(checker))
        count += inner_summ
    return count


if __name__ == '__main__':
    f = open("input_1.txt")
    g = f.readlines()
    print(enigma1(g))
    f.close()

    f = open("input_2.txt")
    g = f.readlines()
    print(enigma2(g))
    f.close()
