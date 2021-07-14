#!/usr/bin/env python3

file = open('data')

for elem in file:
    print(chr(int(elem)), end='')
