#Advent of Code 2022 Day 2
#https://adventofcode.com/2018/day/2

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

data = open('day02.txt')
lines = [line.rstrip() for line in data]
print(len(lines),len(lines[0]),lines[:5])

def part1(testing=False):
    twos,threes = 0,0
    for id in lines:
        id_twos,id_threes = 0, 0
        idset = set(id)
        if testing:
            print(idset)
        for letter in idset:
            if id.count(letter) == 2:
                if testing:
                    print("two:",letter)
                id_twos = 1
            elif id.count(letter) == 3:
                if testing:
                    print("three:", letter)
                id_threes = 1
        twos += id_twos
        threes += id_threes
    print('Part 1:',twos, threes, twos*threes)

def part2(testing=False):
    for idx in range(26):
        for i,box in enumerate(lines):
            for j in range(i+1,len(lines)):
                if testing:
                    print("idx,i,j:",idx,i,j)
                    print(box[:idx]+box[(idx+1):],lines[j][:idx]+lines[j][(idx+1):])
                if box[:idx]+box[(idx+1):] == lines[j][:idx]+lines[j][(idx+1):]:
                    print("Part 2:",box[:idx]+box[(idx+1):])
                    return
    return None

#part1()
part2()

print("Time (s.):",time.time()-start)