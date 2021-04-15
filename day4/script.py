#!/usr/bin/env python3
# coding: utf-8


def checksameval(password):
    p = str(password)
    checker = False
    for i in range(0, len(p)-1):
        if p[i] == p[i+1]:
            checker = True
            return checker
    return checker


def checkincrease(password):
    p = str(password)
    checker = True
    for i in range(0, len(p)-1):
        if p[i] > p[i+1]:
            checker = False
    return checker


def checkpairatleastpresent(password):
    p = str(password) + " "
    previous = p[0]
    currentCount = 1
    numberOfPairs = 0
    for i, e in enumerate(p[1:], start=1):
        if e == previous:
            currentCount += 1
        else:
            if currentCount == 2:
                numberOfPairs += 1
            currentCount = 1
        previous = e
    return numberOfPairs >= 1


def test1(password):
    return checksameval(password) and \
           checkincrease(password)


def test2(password):
    return checksameval(password) and \
           checkincrease(password) and \
           checkpairatleastpresent(password)


if __name__ == '__main__':
    print("Test-u")
    s1 = 111111
    s2 = 223450
    s3 = 123789
    if not test1(s1):
        print("test_p1 1 Failed")
    if test1(s2):
        print("test_p1 2 Failed")
    if test1(s3):
        print("test_p1 3 Failed")
    count = 0
    for i in range(372304, 847060):
        if test1(i):
            count += 1
    print('Answer 1 is ' + str(count))
    s4 = 112233
    s5 = 123444
    s6 = 111122
    if not test2(s4):
        print("test_p1 4 failed")
    if test2(s5):
        print("test_p1 5 failed")
    if not test2(s6):
        print("test_p1 6 failed")
    count = 0
    for i in range(372304, 847060):
        if test2(i):
            count += 1
    print('Answer 2 is ' + str(count))
