#Advent of Code 2022 Day 4
#https://adventofcode.com/2018/day/4

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

day09 = "418 players; last marble is worth 71339 points"

points = 0
def place_marble(n,curr,arr):
    """Places new marble in array. Index of last
    marble is curr"""
    points = 0
    #idx = arr.index(curr)
    if n == 1:
        curr = 0
        arr.insert(1,1)
    elif n % 23 == 0:
        curr = (curr-7)# % len(arr)
        point = arr[curr]
        arr.remove(point)
        points += point + 23

    else:
        #print("old curr:",curr)
        curr = (curr + 2) % (len(arr)+1)
        #print("new curr:",curr)
        #print("old arr:",arr)
        arr.insert(curr, n)
        #print("new arr:", arr)
        #curr += 1

    return curr,arr,points


def part1(numplayers,testing=False):
    curr = 0
    player = 1
    players = {n:0 for n in range(1,numplayers+1)}#419)}
    numlist = list()
    for n in range(1,47):
        curr,arr,points = place_marble(n,curr,numlist)
        if testing:
            print(player,curr,arr,points)
        players[player] += points
        player += 1
        if player == numplayers+1:
            player = 1
    sorted_players = sorted(players.items(), key = lambda x:x[1], reverse = True)
    print(sorted_players)


def part2(testing=False):
    pass

part1(9, True)
#part2()

print("Time (s.):",time.time()-start)