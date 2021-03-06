#!/usr/bin/env python3

import argparse


# Define the parser
parser = argparse.ArgumentParser(description='Script to answer Based questions')

# Declare arguments
parser.add_argument('-2', action='store', dest='bin', default='0')
parser.add_argument('-8', action='store', dest='oct', default='0')
parser.add_argument('-16', action='store', dest='hex', default='00')

# Parse the command line arguments
args = parser.parse_args()


# Convert binary to ASCII
x = args.bin
x = x.split(sep=' ')

for i in x:
    print(chr(int(i, 2)), end='')


# Convert base 8 to ASCII
y = args.oct
y = y.split(sep = ' ')

for i in y:
    print(chr(int(i, 8)), end='')


# Convert base 16 to ASCII
z = args.hex
z = [z[i:i+2] for i in range(0, len(z), 2)]

for i in z:
    print(chr(int(i, 16)), end='')
