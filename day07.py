#Advent of Code 2022 Day 4
#https://adventofcode.com/2018/day/7

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TESTALPHA = 'ABCDEF'

with open('day07.txt') as data:
    lines = [line.rstrip() for line in data]
    before_dict = dict()
    edges = set() #directed graph
    for s in lines:
        s = s.split(' ')
        edges.add((s[1],s[7]))
        if s[7] not in before_dict:
            before_dict[s[7]]= [s[1]]
        else:
            before_dict[s[7]].append(s[1])
    for letter in ALPHA:
        in_arr = False
        if letter not in before_dict:
            print(letter,"not in before_dict.")
        for arr in before_dict.values():
            if letter in arr:
                in_arr = True
                break

        if not in_arr:
            print(letter,"not in values.")

#print(before_dict)
#print(edges)
print(len(lines),lines[:5])

def bfs(letters,testing=False):
    output = ''
    q = deque(letters)
    print("q",q)
    while q:
        if testing:
            print("q:",q)
        #print("Hello")
        newletters = q.popleft()
        if testing:
            print("newletters:",newletters)
        if len(output) == len(letters):
            return output
        for letter in newletters:
            if letter not in before_dict:
                q.append(letter)
            else:
                for let in before_dict[letter]:
                    if let not in output:
                        q.append(letter)

#print(bfs("ABCDEF"),True)

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.verts = list()

    def addEdge(self,u,v):
        self.graph[u].append(v)
        if u not in self.verts:
            self.verts.append(u)
        if v not in self.verts:
            self.verts.append(v)

    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True
        #print("self.graph[v]:",self.graph[v])
        print("sorted:",sorted(self.graph[v]))
        for i in sorted(self.graph[v],reverse=True):
            if not visited[i]:
                print("util:",i,visited,stack)
                self.topologicalSortUtil(i,visited,stack)
        stack.append(v)
        print("stack:",stack)

    def topologicalSort(self):
        visited = {i:False for i in self.verts}
        stack = list()
        print("self.verts:",self.verts)
        for v in sorted(self.verts,reverse=True):
            if not visited[v]:
                self.topologicalSortUtil(v,visited,stack)

        print("stack:",''.join(stack[::-1]))

def topo_sort(letter ='A',output = ''):
    """From Geeks for Geeks tutorial https://www.geeksforgeeks.org/topological-sorting/"""
    #Create a stack to store the nodes
    letters = 'ABCDEF'
    #initialize visited array of size N to keep track of visited nodes:
    #visited = {letter: False for letter in letters}

    for i,v in enumerate(letters):
        if v not in before_dict and v not in output:
            output += v
        else:
            output += v


def part1(testing=False):
    g = Graph(101)
    for e in edges:
        g.addEdge(e[0],e[1])
    print("g:",g.graph)
    g.topologicalSort() #NYIZHFMUOBTXKQRJDASGPVCEWL not correct
    #ZYNMOTUIKHFRBQXJDSAGPECVWL also not correct
    #MNOUBYITKXZFRJDSHQAGCPEVWL also not correct
    #MNOUBYITKXZFHQRJDASGCPEVWL correct! Thx JP



def part2(testing=False):
    pass

part1()
#part2()

print("Time (s.):",time.time()-start)