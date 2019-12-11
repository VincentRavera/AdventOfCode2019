#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import re
import matplotlib.pyplot as plt


class Grid():
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((size, size))
        self.center = (int(np.floor(size/2)), int(np.floor(size/2)))
        self.matrix[self.center] = -10

    def U(self, posx, posy, y, amp=10):
        self.matrix[posy-y:posy+1, posx] += amp
        self.matrix[posy, posx] -= amp
        return posx, posy - y

    def D(self, posx, posy, y, amp=10):
        self.matrix[posy:posy+y+1, posx] += amp
        self.matrix[posy, posx] -= amp
        return posx, posy + y

    def R(self, posx, posy, x, amp=10):
        self.matrix[posy, posx:posx+x+1] += amp
        self.matrix[posy, posx] -= amp
        return posx + x, posy

    def L(self, posx, posy, x, amp=10):
        self.matrix[posy, posx-x:posx+1] += amp
        self.matrix[posy, posx] -= amp
        return posx - x, posy

    def maxValuesPostion(self, crossVal=0):
        if crossVal == 0:
            crossVal = np.amax(self.matrix)
        val = np.transpose(np.where(self.matrix == crossVal))
        if len(val) == 0:
            return None
        return val

    def manhattan(self, crossVal=0):
        vals = self.maxValuesPostion(crossVal=crossVal)
        dists = []
        for val in vals:
            posx = val[0]
            posy = val[1]
            dist = np.abs(self.center[0] - posx) + \
                np.abs(self.center[0] - posy)
            dists.append(int(dist))
        return dists

    def simple_manhattan(self, xy1, xy2):
        return np.abs(xy1[0] - xy2[0]) + \
            np.abs(xy1[1] - xy2[1])

    def parseInputs(self,
                    inputs,
                    amplitude=10,
                    notifypoints=None,
                    debug=False):
        directions = re.split(',', inputs)
        udrl = re.compile("^\w")  # noqa W605
        vals = re.compile("\d+$")  # noqa W605
        current_posx = int(self.center[0])
        current_posy = int(self.center[1])
        for direction in directions:
            letter = udrl.search(direction).group()
            value = int(vals.search(direction).group())
            if debug:
                print(letter, str(value))
            if letter == 'U':
                current_posx, current_posy = self.U(
                                                    current_posx,
                                                    current_posy,
                                                    value,
                                                    amp=amplitude)
            elif letter == 'D':
                current_posx, current_posy = self.D(
                                                    current_posx,
                                                    current_posy,
                                                    value,
                                                    amp=amplitude)
            elif letter == 'R':
                current_posx, current_posy = self.R(
                                                    current_posx,
                                                    current_posy,
                                                    value,
                                                    amp=amplitude)
            elif letter == 'L':
                current_posx, current_posy = self.L(
                                                    current_posx,
                                                    current_posy,
                                                    value,
                                                    amp=amplitude)
            else:
                raise Exception("Unparsable input :" + direction)
            if debug:
                plt.imshow(self.matrix)
                plt.show()

    def move(self, letter, value, current_posx, current_posy, amplitude=10):
        if letter == 'U':
            current_posx, current_posy = self.U(
                                                current_posx,
                                                current_posy,
                                                value,
                                                amp=amplitude)
        elif letter == 'D':
            current_posx, current_posy = self.D(
                                                current_posx,
                                                current_posy,
                                                value,
                                                amp=amplitude)
        elif letter == 'R':
            current_posx, current_posy = self.R(
                                                current_posx,
                                                current_posy,
                                                value,
                                                amp=amplitude)
        elif letter == 'L':
            current_posx, current_posy = self.L(
                                                current_posx,
                                                current_posy,
                                                value,
                                                amp=amplitude)
        else:
            raise Exception("Unparsable input :" + letter)
        return current_posx, current_posy

    def stepbystep(self, input1, input2):
        directions_1 = re.split(',', input1)
        directions_2 = re.split(',', input2)
        udrl = re.compile("^\w")  # noqa W605
        vals = re.compile("\d+$")  # noqa W605
        c_posx_1 = int(self.center[0])
        c_posy_1 = int(self.center[1])
        c_posx_2 = int(self.center[0])
        c_posy_2 = int(self.center[1])
        count_1 = 0
        count_2 = 0
        for i in range(0, len(directions_1)):
            letter_1 = udrl.search(directions_1[i]).group()
            value_1 = int(vals.search(directions_1[i]).group())
            letter_2 = udrl.search(directions_2[i]).group()
            value_2 = int(vals.search(directions_2[i]).group())
            c_posx_1, c_posy_1 = self.move(letter_1, value_1,
                                           c_posx_1, c_posy_1, amplitude=5)
            c_posx_2, c_posy_2 = self.move(letter_2, value_2,
                                           c_posx_2, c_posy_2, amplitude=50)
            intersec = self.maxValuesPostion(crossVal=55)
            count_1 += value_1
            count_2 += value_2
            if intersec is not None and len(intersec) == 1:
                # print("Intersec is at =" + str(intersec))
                # print("pos1 is at =" + str((c_posx_1, c_posy_1)))
                # print("pos2 is at =" + str((c_posx_2, c_posy_2)))
                # print("count1 is at =" + str(count_1))
                # print("count2 is at =" + str(count_2))
                print("Raw :" + str(count_1 + count_2))
                count_1 -= self.simple_manhattan(intersec[0],
                                                 (c_posy_1, c_posx_1))
                print("we cut " + str(self.simple_manhattan(intersec[0],
                                      (c_posy_1, c_posx_1))) + "of 1")
                count_2 -= self.simple_manhattan(intersec[0],
                                                 (c_posy_2, c_posx_2))
                print("we cut " + str(self.simple_manhattan(intersec[0],
                                      (c_posy_2, c_posx_2))) + "of 2")
                break
        return count_1 + count_2

    def showimg(self):
        plt.imshow(self.matrix)
        plt.show()


def test1():
    print("Test-U-1")
    test11 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    test12 = "U62,R66,U55,R34,D71,R55,D58,R83"
    grid = Grid(512)
    grid.parseInputs(test11, amplitude=5)
    grid.parseInputs(test12, amplitude=50)
    out = min(grid.manhattan(55))
    if out != 159:
        print("Error for Test-u 1: expected 159, got " + str(out))
    return grid


def test2():
    print("Test-U-2")
    test11 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    test12 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    grid = Grid(512)
    grid.parseInputs(test11, amplitude=5)
    grid.parseInputs(test12, amplitude=5)
    out = min(grid.manhattan())
    if out != 135:
        print("Error for Test-u 1: expected 135, got " + str(out))
    return grid


def test3():
    print("Test-U-3")
    test11 = "R8,U5,L5,D3"
    test12 = "U7,R6,D4,L4"
    grid = Grid(20)
    grid.parseInputs(test11)
    grid.parseInputs(test12)
    out = min(grid.manhattan())
    if out != 6:
        print("Error for Test-u 1: expected 6, got " + str(out))
    return grid


if __name__ == '__main__':
    print("Test-U")
    t1 = test1()
    t2 = test2()
    t3 = test3()
    test41 = "R8,U5,L5,D3"
    test42 = "U7,R6,D4,L4"
    grid = Grid(512)
    t4 = grid.stepbystep(test41, test42)
    if t4 != 30:
        print("Test 4 failed expected 30 got " + str(t4))
    test51 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    test52 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    grid = Grid(512)
    t5 = grid.stepbystep(test51, test52)
    if t5 != 410:
        print("Test 5 failed expected 410 got " + str(t5))
    test61 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    test62 = "U62,R66,U55,R34,D71,R55,D58,R83"
    grid = Grid(512)
    t6 = grid.stepbystep(test61, test62)
    if t6 != 610:
        print("Test 6 failed expected 610 got " + str(t6))
    print("End Test-U")

    # f = open('inputs1.txt')
    # input1 = f.readline()
    # input2 = f.readline()
    # f.close()
    # g = Grid(25000)
    # print(str(g.stepbystep(input1, input2)))
