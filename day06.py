#Advent of Code 2022 Day 4
#https://adventofcode.com/2018/day/4

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import operator
import time

start = time.time()

with open('day06.txt') as data:
    lines = [line.rstrip() for line in data]
    locs = list()
    for pair in lines:
        x = pair.split(',')
        locs.append((int(x[0]),int(x[1])))
print(len(locs),locs[:5])
minx,maxx,miny,maxy = 1000,0,1000,0
n,e,s,w = None,None,None,None #NESW-most locations
for loc in locs:
    if loc[0] < minx:
        minx = loc[0]
        w = loc
    elif loc[0] > maxx:
        maxx = loc[0]
        e = loc
    elif loc[1] < miny:
        miny = loc[1]
        n = loc
    elif loc[1] > maxy:
        maxy = loc[1]
        s = loc
print("minx,maxx,miny,maxy:",minx,maxx,miny,maxy,n,e,s,w)

def mdist(a,b):
    """Returns the Manhattan distance between a and b"""
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def closest_point(p):
    """Returns the closest point to point p"""
    min_dist = 10000
    closest = None
    tie = False
    for loc in locs:
        d = mdist(p,loc)
        if d < min_dist:
            min_dist = d
            closest = loc
            tie = False
        elif d == min_dist:
            tie = True

    if not tie:
        return closest
    else:
        return None

def total_distances(a):
    """Returns True if sum of distances from a
    to all locs is less than 10000."""
    dists = 0
    for l in locs:
        dists += mdist(a, l)
        if dists >= 10000:
            return False
    return True

def def_value():
    return 0
def part1(testing=False):
    locs_dict = defaultdict(def_value)
    border_locs = set()
    for x in range(40,350):
        for y in range(50,360):
            closest = closest_point((x, y))
            locs_dict[closest] += 1
            if testing:
                print("x,y:",x,y)
            #if location is on the border
            if y in [50,360]:
                border_locs.add(closest)
    max_value = max(locs_dict.values())  # maximum value
    max_keys = [k for k, v in locs_dict.items() if v == max_value]
    sorted_locs = sorted(locs_dict.items(), key=operator.itemgetter(1),reverse=True)
    # for loc in sorted_locs:
    #     if loc in border_locs:
    #         sorted_locs.remove(loc)
    print("Part 1:",max_keys,max_value)
    print("sorted_locs:",sorted_locs[:10])

def part2(testing=False):
    total = 0
    for x in range(40, 350):
        for y in range(50, 360):
            loc = (x,y)
            if total_distances(loc):
                total += 1
    print("Part 2:",total)





#part1() #5338 and 4885 too high, 2491 too low
part2() #50530

print("Time (s.):",time.time()-start)