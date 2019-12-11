#!/usr/bin/env python3
# coding: utf-8
import re


class OpCode():
    def __init__(self, li):
        self.li = li
        self.pos = 0

    def read_at_pos(self, x):
        val = self.li[x]
        if val == 1:
            y = self.op1(x)
        elif val == 2:
            y = self.op2(x)
        else:
            return
        # return self.read_at_pos(y)
        return self.read_at_pos(y)

    def get_pointer_value(self, x):
        pointer = self.li[x]
        value = self.li[pointer]
        return value

    def op1(self, x):
        value = self.get_pointer_value(x+1) + \
                self.get_pointer_value(x+2)
        self.li[self.li[x+3]] = value
        return x + 4

    def op2(self, x):
        value = self.get_pointer_value(x+1) * \
                self.get_pointer_value(x+2)
        self.li[self.li[x+3]] = value
        return x + 4


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
    print("Test-U")
    input_str = "1,9,10,3,2,3,11,0,99,30,40,50"
    validating_str = "3500,9,10,70,2,3,11,0,99,30,40,50"
    print(validate(input_str, validating_str))
    input_str = "1,0,0,0,99"
    validating_str = "2,0,0,0,99"
    print(validate(input_str, validating_str))
    a = "2,3,0,3,99"
    a1 = "2,3,0,6,99"
    b = "2,4,4,5,99,0"
    b1 = "2,4,4,5,99,9801"
    c = "1,1,1,4,99,5,6,0,99"
    c1 = "30,1,1,4,2,5,6,0,99"
    print(validate(a, a1))
    print(validate(b, b1))
    print(validate(c, c1))
    f = open("input1.txt")
    g = f.readline()
    h = format_str_2_li(g)
    h[1] = 12
    h[2] = 2
    code = OpCode(h)
    code.read_at_pos(0)
    print(str(code.li[0]))
    f.close()
    f = open("input2.txt")
    g = f.readline()
    h = format_str_2_li(g)
    code = None
    for noun in range(0, 100):
        for verb in range(0, 100):
            h[1] = noun
            h[2] = verb
            code = OpCode(h[::])
            code.read_at_pos(0)
            if code.li[0] == 19690720:
                print("noun: " + str(noun) + "verb: " + str(verb))
            code = None
    f.close()
