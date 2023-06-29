#Advent of Code 2022 Day 7
#https://adventofcode.com/2018/day/7
#Jonathan Paulson's video tutorial
#https://www.youtube.com/watch?v=ztRDsq1qJlc&t=285s

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

E = defaultdict(list)
D = defaultdict(int)
for line in open('day07.txt'):
    words = line.split()
    x = words[1]
    y = words[7]
    E[x].append(y)
    D[y]+= 1

Q = deque()
for k in E:
    if D[k] == 0:
        Q.append(k)

ans = ''
while Q:
    print("Q:",Q)
    x = sorted(Q)[0]
    Q = [y for y in Q if y!=x]
    ans+=x
    for y in E[x]:
        D[y] -=1
        if D[y] == 0:
            Q.append(y)
print("Part 1:",ans)

print(len(lines),lines[:5])

def part1(testing=False):
    pass

def part2(testing=False):
    pass

part1()
#part2()

print("Time (s.):",time.time()-start)