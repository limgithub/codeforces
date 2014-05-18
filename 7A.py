#!/usr/bin/env python2.7
import sys

num_vertical = 0
num_horizon = 0

for line in sys.stdin:
    if line.count('W'):
        num_horizon = line.count('B')
    else:
        num_vertical += 1

print num_vertical + num_horizon
