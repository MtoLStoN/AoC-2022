#!/bin/python3

import sys
import copy as cp

class Node:
    def __init__(self,x,y,isWall,isSand):
        self.x = x
        self.y = y
        self.name=str(x)+","+str(y)
        self.isWall = isWall
        self.isSand = isSand
        self.isRested = False
def get_node(map,x,y):
    name=str(x)+","+str(y)
    for i in range(len(map)):
        if map[i].name == name:
            return map[i]
    map.append(Node(x,y,False,False))
    return map[-1]
def add_node(map,node):
    for nodes in map:
        if nodes.x == node.x and nodes.y == node.y:
            return
    map.append(node)
def draw_map(map1):
    drawn=[[] for i in range(floor)]
    for y in range(0,floor):
        for x in range(width[0],width[1]):
            node=get_node(map1,x,y)
            if node.isWall:
                drawn[y].append("#")
            elif node.isSand and not node.isRested:
                drawn[y].append("+")
            elif node.isRested:
                drawn[y].append("o")
            else:
                drawn[y].append(".")
    return drawn
    
with open(sys.argv[1],"r") as f:
    lines = f.readlines()

map = []
abyss = 0
width=[500,500]

for line in lines:
    walls = line.strip().split("->")
    for i in range(0,len(walls)-1):
        coord1 = [int(x) for x in walls[i].split(",")]
        coord2 = [int(x) for x in walls[i+1].split(",")]
        rx=1
        ry=1
        if coord2[0] < coord1[0]:
            rx=-1
        if coord2[1] < coord1[1]:
            ry=-1
        for x in range(coord1[0],coord2[0]+rx,rx):
            for y in range(coord1[1],coord2[1]+ry,ry):
                add_node(map,Node(x,y,True,False))
                if y > abyss:
                    abyss = y
                if x > width[1]:
                    width[1]=x
                if x < width[0]:
                    width[0]=x

map.append(Node(500,0,False,True))

map2=cp.deepcopy(map)

print("The abyss starts at: "+str(abyss))
floor=abyss+2
node=get_node(map,500,0)

units=0

path=[]

while True:
    path.append(node)
    if not node.isSand:
        print("Error: Sand not found")
        break
    if node.isSand and not node.isRested:
        node.isSand=False
        down=get_node(map,node.x,node.y+1)
        if not down.isWall and not down.isRested:
            node=down
            node.isSand=True
        else:
            left=get_node(map,node.x-1,node.y+1)
            if not left.isWall and not left.isRested:
                node=left
                node.isSand=True
            else:
                right=get_node(map,node.x+1,node.y+1)
                if not right.isWall and not right.isRested:
                    node=right
                    node.isSand=True
                else:
                    node.isRested=True
                    node.isSand=True
    if node.isRested:
        if path == []:
            node=get_node(map2,500,0)
        else:
            node=path[-2]
        path=path[:-2]
        node.isSand=True
        units+=1
    if node.y > abyss:
        break
    print("Simulating "+str(units)+" units of sand.",end="\r")
print(str(units)+ " units of sand were needed to reach the abyss")

print("The floor is at: "+str(floor))

node=get_node(map2,500,0)

units=0

path=[]

while True:
    path.append(node)
    if not node.isSand:
        print("Error: Sand not found")
        break
    if node.isSand and not node.isRested:
        node.isSand=False
        down=get_node(map2,node.x,node.y+1)
        if not down.isWall and not down.isRested and not down.y >= floor:
            node=down
            node.isSand=True
        else:
            left=get_node(map2,node.x-1,node.y+1)
            if not left.isWall and not left.isRested and not left.y >= floor:
                node=left
                node.isSand=True
            else:
                right=get_node(map2,node.x+1,node.y+1)
                if not right.isWall and not right.isRested and not right.y >= floor:
                    node=right
                    node.isSand=True
                else:
                    node.isRested=True
                    node.isSand=True
    if node.isRested:
        try:
            node=path[-2]
        except:
            node=get_node(map2,500,0)
        path=path[:-3]
        units+=1
        if node.isSand:
            break
        node.isSand=True
    print("Simulating "+str(units)+" units of sand.",end="\r")
print(str(units)+ " units of sand were needed for a safe stand.")
print('\n'.join(map(''.join, draw_map(map2))))
