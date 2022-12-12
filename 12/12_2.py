#!/bin/python3

import sys
import numpy as np
import random

class map:
    def __init__(self,Target,height,distance):
        self.visited=False
        self.height=height
        self.target=Target
        self.distance=distance


lines=open(sys.argv[1]).readlines()

paths = []

maps = [[] for _ in range(0,len(lines))]

for i in range(0,len(lines)):
    line=lines[i].strip()
    for j in range(0,len(line)):
        if line[j] == 'S':
            start=[j,i]
            maps[i].append(map(False,97,0))
        elif line[j] == 'E':
            maps[i].append(map(True,122,1000))
        else:
            maps[i].append(map(False,ord(line[j]),1000))

curr=start
starting_nodes=[]
for x in range(0,len(maps[0])):
    for y in range(0,len(maps)):
        if maps[y][x].height == 97:
            starting_nodes.append([x,y])

paths=[]
for node in starting_nodes:
    nodes=[node]
    for x in range(0,len(maps[0])):
        for y in range(0,len(maps)):
            maps[y][x].visited=False
            maps[y][x].distance=1000
    maps[node[1]][node[0]].distance=0
    while True:
        for curr in nodes:
            if maps[curr[1]][curr[0]].visited:
                nodes.remove(curr)
                continue
            x=curr[0]
            y=curr[1]
            moves = [[-1,0],[1,0],[0,-1],[0,1]]
            for move in moves:
                coordinates = [x+move[0],y+move[1]]
                if x+move[0] in range(0,len(maps[0])) and y+move[1] in range(0,len(maps)):
                    if maps[coordinates[1]][coordinates[0]].visited == False:
                        if maps[y+move[1]][x+move[0]].height in range(maps[y][x].height-2,maps[y][x].height+2):
                            if maps[y][x].distance+1 < maps[y+move[1]][x+move[0]].distance:
                                maps[y+move[1]][x+move[0]].distance=maps[y][x].distance+1
                                nodes.append(coordinates)
            maps[y][x].visited=True
        if nodes == []:
            break

    for x in range(0,len(maps[0])):
        for y in range(0,len(maps)):
            if maps[y][x].target:
                paths.append(maps[y][x].distance)

paths.sort()
print(paths[0])

