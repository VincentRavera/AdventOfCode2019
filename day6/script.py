#!/usr/bin/env python3
# coding: utf-8


def appendCount(catalog, chain, position):
    chain.append(position)
    new_pos = catalog[position]
    if new_pos != "COM":
        return appendCount(catalog, chain, new_pos)
    else:
        return chain


def countOrbit(catalog, starting):
    chain = []
    appendCount(catalog, chain, starting)
    return len(chain)


if __name__ == '__main__':
    # catalog = {}
    # with open('input_test.txt') as f:
    #     for line in f.readlines():
    #         A, B = line.split(')')
    #         catalog[str.rstrip(B)] = (str.rstrip(A))
    # count = 0
    # for key in catalog.keys():
    #     count += countOrbit(catalog, key)
    # print(count)
    # catalog = {}
    # with open('input.txt') as f:
    #     for line in f.readlines():
    #         A, B = line.split(')')
    #         catalog[str.rstrip(B)] = (str.rstrip(A))
    # count = 0
    # for key in catalog.keys():
    #     count += countOrbit(catalog, key)
    # print(count)
    catalog = {}
    with open('input.txt') as f:
        for line in f.readlines():
            A, B = line.split(')')
            catalog[str.rstrip(B)] = (str.rstrip(A))
    youchain = []
    appendCount(catalog, youchain, 'YOU')
    sanchain = []
    appendCount(catalog, sanchain, 'SAN')
    fcn = None
    for ucheck in youchain:
        for scheck in sanchain:
            if ucheck == scheck:
                fcn = ucheck
                break
        if fcn is not None:
            break
    print(countOrbit(catalog, "YOU") - countOrbit(catalog, fcn) +
          countOrbit(catalog, "SAN") - countOrbit(catalog, fcn) - 2)
