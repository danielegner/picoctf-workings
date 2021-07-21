#!/usr/bin/env python3

with open('lyrics.txt') as f:
    data = f.read()

stripped = ''.join(data.split()).replace('i', '1')

print('picoCTF{', stripped, '}', sep='')
