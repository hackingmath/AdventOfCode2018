#Advent of Code 2022 Day
#https://adventofcode.com/2018/day/

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

data = open('day03.txt')
lines = [line.rstrip() for line in data]
lines = [l.split(' ') for l in lines]
print(len(lines),lines[:5])
grid_dict = dict()
dupe_set = set()
not_dupe_set = {i for i in range(1,len(lines)+1)}
#print("not dupe set:",not_dupe_set)
def populate_arr(input_arr,testing=False):
    """Populates dict of coordinates covered by rectangles
    at given location with given dimensions"""
    arr = dict() #grid dictionary
    for claim in input_arr:
        print("not dupe set:",not_dupe_set)
        claim_num = int(claim[0][1:])
        if testing:
            print("claim_num:",claim_num)
        x,y = map(int,claim[2][:-1].split(','))
        w,h = map(int,claim[3].split('x'))
        if testing:
            print("x,y,w,h",x,y,w,h)
        for i in range(w):
            for j in range(h):
                if (x+i,y+j) in arr:
                    if testing:
                        print("dupe:",(x+i,y+j))
                    arr[(x + i, y + j)] += 1
                    if (x+i,y+j) not in dupe_set:
                        dupe_set.add((x+i,y+j))
                    if claim_num in not_dupe_set:
                        not_dupe_set.remove(claim_num)
                else:
                    arr[(x + i, y + j)] = 1

#populate_arr(grid_dict)
def part1(testing=False):
    populate_arr(lines,testing)
    populate_arr(lines[::-1],testing)
    print("Part 1:", not_dupe_set, len(not_dupe_set))

def part2(testing=False):
    pass

part1()
#part2()

print("Time (s.):",time.time()-start)