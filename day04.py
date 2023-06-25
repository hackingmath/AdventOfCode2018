#Advent of Code 2022 Day 4
#https://adventofcode.com/2018/day/4

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time
from datetime import datetime

start = time.time()

data = open('day04.txt')
lines = [line.rstrip() for line in data]
sorted_arr = sorted(lines)#[n.split(" ") for n in lines])
print(len(sorted_arr),sorted_arr[:10])

def part1(testing=False):
    d1 = datetime.strptime('18-03-13 23:56',
                  '%y-%m-%d %H:%M')
    d2 = datetime.strptime('18-03-14 00:43',
                  '%y-%m-%d %H:%M')
    print(d2-d1)

def part2(testing=False):
    pass

part1()
#part2()

print("Time (s.):",time.time()-start)