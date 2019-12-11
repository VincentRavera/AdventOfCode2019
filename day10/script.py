#!/usr/bin/env python3
# coding: utf-8
import numpy as np


def parseInputs(text_file):
    with open(text_file) as f:
        g = f.readlines()
        a = np.zeros((len(g[0]), len(g)))
        for x, i in enumerate(g[:]):
            line = str(i).rstrip()
            for y, j in enumerate(line):
                if j == "#":
                    a[x, y] = 1
    return a


class AsteroidField:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def getVector():
        return [0, 1]

    def getLineOfSight(self, position, vector):
        pass


if __name__ == '__main__':
    f1 = AsteroidField(parseInputs('input1.txt'))
    f1.getLineOfSight((0, 0), f1.getVector())
