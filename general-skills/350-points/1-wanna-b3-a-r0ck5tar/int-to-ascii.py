#!/usr/bin/env python3

print('picoCTF{', end='')

with open('rockstar-output.txt', 'r') as f:
    for elem in f:
        print(chr(int(elem)), end='')

print('}')
