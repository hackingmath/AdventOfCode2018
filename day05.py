#Advent of Code 2022 Day 5
#https://adventofcode.com/2018/day/5

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

with open('day05.txt') as data:
    lines = [line for line in data]
print(len(lines))

def part1(instr,testing=False):
    newstr = ''
    changes = 1
    while changes != 0:
        changes = 0
        changing = False
        for i,s in enumerate(instr):
            if i == len(instr) - 1:
                newstr += s
                break
            if not changing and s.lower() != instr[i+1].lower():
                newstr += s
            elif s != instr[i+1] and not changing:
                changing = True
                continue
            else:
                changing = False
                changes += 1
                continue
        print("newstr:",newstr)
        instr,newstr = newstr, ''
    print("Part 1:",len(instr))



def part2(testing=False):
    pass

teststr = 'dabAcCaCBAcCcaDA'
part1(lines[0]) #11968 too high
#part2()

print("Time (s.):",time.time()-start)