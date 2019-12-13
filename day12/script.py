#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import re
import matplotlib.pyplot as plt
import time


class OrbitalSystem:
    def __init__(self, path):
        data = self.readInputs(path)
        self.asteroids = np.zeros((len(data), 2, 3))
        for i, line in enumerate(data):
            x = re.search('(x)=([0-9-]*)', line)
            y = re.search('(y)=([0-9-]*)', line)
            z = re.search('(z)=([0-9-]*)', line)
            self.asteroids[i, 0, 0] = int(x.group(2))
            self.asteroids[i, 0, 1] = int(y.group(2))
            self.asteroids[i, 0, 2] = int(z.group(2))
        self.init_pos = np.copy(self.asteroids[:])

    def updateVelocity(self):
        for asteroid_id in range(len(self.asteroids)):
            v_xyz = self.asteroids[asteroid_id, 1]
            p_xyz = self.asteroids[asteroid_id, 0]
            for xyz in range(0, len(v_xyz)):
                axis = list(self.asteroids[:, 0, xyz][:])
                axis.pop(asteroid_id)
                for other_ast in range(0, len(axis)):
                    if p_xyz[xyz] > axis[other_ast]:
                        v_xyz[xyz] -= 1
                    elif p_xyz[xyz] < axis[other_ast]:
                        v_xyz[xyz] += 1

    def updatePosition(self):
        for asteroid_id in range(len(self.asteroids)):
            v_xyz = self.asteroids[asteroid_id, 1]
            p_xyz = self.asteroids[asteroid_id, 0]
            p_xyz += v_xyz

    def compute(self):
        self.updateVelocity()
        self.updatePosition()

    def iterate(self, num_step):
        for i in range(0, num_step):
            self.compute()
        print("Total E: ", self.calc_total_energy())

    def showEnergy(self):
        try:
            start = time.time()
            counter = 2
            self.compute()
            while not self.is_kine_zero():
                self.compute()
                counter += 1
            print("Kine is null")
        finally:
            end = time.time()
            print("Stopped at :" + str(counter) + " in " + str(end - start) + "s.")

    def reset(self):
        self.asteroids = np.copy(self.init_pos[:])

    @staticmethod
    def readInputs(path):
        with open(path) as f:
            data = f.readlines()
        return data

    def calc_total_energy(self):
        abs_pos = abs(self.asteroids[:, 0, :])
        abs_vel = abs(self.asteroids[:, 1, :])
        total = 0
        for i in range(0, len(abs_pos)):
            total += sum(abs_pos[i]) * sum(abs_vel[i])
        return total

    def is_kine_zero(self):
        # return hash(str(self.asteroids[:, 0, :])) == hash(str(self.init_pos[:, 0, :]))
        return np.sum(self.asteroids[:, 0, :] == self.init_pos[:, 0, :]) == 12

    def test_compute(self, iters):
        start = time.time()
        self.iterate(iters)
        end = time.time()
        print(str(iters) + " iters took " + str(end - start) + "s.")
        print("Score is ", (end - start) / iters)
        return end - start

    def plot_perf(self):
        x = []
        y = []
        for i in range(0, 10000, 1000):
            x.append(i)
            y.append(self.test_compute(i))
        plt.plot(x, y)
        plt.show()


class OS2(OrbitalSystem):

    def updateVelocity(self):
        for id_ast, v_ast in enumerate(self.asteroids[:, 1, :]):
            for xyz, v_ast_xyz in enumerate(v_ast):
                axis = nabs(self.asteroids[:, 0, xyz] - self.asteroids[id_ast, 0, xyz], id_ast)
                self.asteroids[id_ast, 1, xyz] += sum(axis)


def nabs(a, aste):
    b = abs(a)
    b[aste] = 1
    return a / b


if __name__ == '__main__':
    test = OrbitalSystem('test_1.txt')
    test.test_compute(50000)

    test = OS2('test_1.txt')
    test.test_compute(50000)
    # test = OrbitalSystem('test2.txt')
    # test.showEnergy()
