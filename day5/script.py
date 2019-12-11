#!/usr/bin/env python3
# coding: utf-8
import re


class OpCode():
    def __init__(self, li, input_integer=1, mode=0):
        self.li = li
        self.pos = 0
        self.input_integer = input_integer
        self.mode = mode
        self.queue = list()
        self.count = 0

    def read_at_pos(self, x):
        self.read_fi(x)
        val = self.li[x]
        if val == 1:
            y = self.op1(x)
        elif val == 2:
            y = self.op2(x)
        elif val == 3:
            y = self.op3(x)
        elif val == 4:
            y = self.op4(x)
        else:
            print("Error op code was: ", str(val), "at instruct: ", str(self.count)) # noqa E501
            return
        self.count += 1
        return self.read_at_pos(y)

    def get_pointer_value(self, x):
        if self.mode == 1:
            return self.li[x]
        else:
            pointer = self.li[x]
            value = self.li[pointer]
            return value

    def set_pointer_value(self, x, val):
        if self.mode == 0:
            self.li[self.li[x]] = val
        elif self.mode == 1:
            self.li[self.li[x]] = val

    def op1(self, x):
        print("OP1")
        self.nextmode()
        value = self.get_pointer_value(x+1) + \
            self.get_pointer_value(x+2)
        self.set_pointer_value(x+3, value)
        return x + 4

    def op2(self, x):
        print("OP2")
        self.nextmode()
        value = self.get_pointer_value(x+1) * \
            self.get_pointer_value(x+2)
        self.set_pointer_value(x+3, value)
        return x + 4

    def op3(self, x):
        print("OP3")
        self.nextmode()
        value = self.get_pointer_value(x+1)
        self.li[value] = self.input_integer
        return x + 2

    def op4(self, x):
        print("OP4")
        self.nextmode()
        value = self.get_pointer_value(x)
        self.output_integer = value
        print(value)
        return x + 2

    def read_fi(self, x):
        instruct = str(self.li[x])
        if len(instruct) > 1:
            self.li[x] = int(re.search('\d\d$', instruct).group())  # noqa W605
            modes, = re.search('(.*)\d\d$', instruct).groups()  # noqa W605
            self.queue = list(modes)

    def nextmode(self):
        if len(self.queue) > 0:
            self.mode = int(self.queue.pop())
        else:
            self.mode = 0


def validate(input_str, validating_str):
    g = re.split(',', input_str)
    o = re.split(',', validating_str)
    for i in range(0, len(g)):
        g[i] = int(g[i])
        o[i] = int(o[i])
    Testu = OpCode(g)
    Testu.read_at_pos(0)
    for i in range(0, len(g)):
        if o[i] != Testu.li[i]:
            raise Exception("Fail at pos: " + str(i))
    return True


def format_str_2_li(s):
    h = re.split(',', g)
    for i in range(0, len(h)):
        h[i] = int(h[i])
    return h


def format_li_2_str(li):
    s = ""
    for i in li:
        s += str(i) + ","
    return s


if __name__ == '__main__':
    f = open("input1.txt")
    g = f.readline()
    f.close()
    h = format_str_2_li(g)
    code = OpCode(h[:], input_integer=1)
    code.read_at_pos(0)
