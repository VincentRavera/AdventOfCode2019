#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


class Image:
    def __init__(self, num_x, num_y, data):
        self.num_y = num_y
        self.num_x = num_x
        self.raw_data = data
        self.data = np.zeros((int(len(self.raw_data) / (self.num_x * self.num_y)), self.num_y, self.num_x))
        self.compute_data()

    def compute_data(self):
        for num_layer in range(0, int(len(self.raw_data) / (self.num_x * self.num_y))):
            layer = self.raw_data[
                    num_layer * self.num_y * self.num_x:num_layer * self.num_y * self.num_x + self.num_y * self.num_x]
            for num_row in range(0, int(len(layer) / self.num_y)):
                row = layer[num_row * self.num_x:num_row * self.num_x + self.num_x]
                for num_pix, pix in enumerate(row[:]):
                    self.data[num_layer, num_row, num_pix] = int(pix)

    def get_fewest_zero_layer(self):
        least_zero = 999999999
        least_num = 999999999
        for num_layer in range(0, len(self.data)):
            layer = self.data[num_layer]
            zeroes = len(np.where(layer == 0)[0])
            if zeroes < least_zero:
                least_zero = zeroes
                least_num = num_layer
        return self.data[least_num]

    @staticmethod
    def get_numbers_of_value(value, layer):
        return len(np.where(layer == value)[0])

    def get_p1(self):
        layer = self.get_fewest_zero_layer()
        print(str(self.get_numbers_of_value(1, layer) * self.get_numbers_of_value(2, layer)))

    def get_p2(self):
        layer = self.add_layers()
        plt.imshow(layer)
        plt.show()

    def add_layers(self):
        layer = np.zeros((self.num_y, self.num_x))
        for i in range(0, self.num_y):
            for j in range(0, self.num_x):
                value = 2
                for val in self.data[:, i, j]:
                    if val == 1:
                        value = 1
                        break
                    elif val == 0:
                        value = 0
                        break
                layer[i, j] = value
        return layer


if __name__ == '__main__':
    test_1 = Image(3, 2, '120021212000')
    test_1.get_fewest_zero_layer()
    with open('input.txt') as f:
        stri = f.readline()
    realData = Image(25, 6, stri)
    realData.get_p2()
