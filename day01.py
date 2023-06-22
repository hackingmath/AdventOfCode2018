#Advent of Code 2022 Day 18
#https://adventofcode.com/2018/day/1

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

data = open('day01.txt').read().strip()
lines = [x for x in data.split('\n')]
print(lines)

def part1(testing=False):
    print(sum(map(int,lines)))
    return
    freq = 0
    for change in lines:
        if change[0] == '-':
            freq -= int(change[1:])
        else:
            freq += int(change[1:])
    print("Part 1:",freq)

testlines = ['+7', '+7', '-2', '-7', '-4']
def part2(testing=False):
    freq = 0
    freqs = {0}
    while True:
        for change in lines:
            if change[0] == '-':
                freq -= int(change[1:])
            else:
                freq += int(change[1:])
            if testing:
                print("freq:",freq)
            if freq in freqs:
                print("Part 2:", freq)
                return
            else:
                freqs.add(freq)

part1()
#part2()

print("Time (s.):",time.time()-start)