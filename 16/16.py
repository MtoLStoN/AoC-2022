#!/bin/python3.9

import sys
import copy as cp
from tqdm import tqdm

class valve:
    def __init__(self,name,flow):
        self.connections=[]
        self.name=name
        self.flow=flow
        self.isopen=False
        
#Steps to target from position
def steps(start,target,visited):
    min_step=1000
    visited.append(start)
    visit=len(visited)
    for tunnel in start.connections:
        if target in tunnel:
            return 1
    for tunnel in start.connections:
        if tunnel[0] not in visited:
            tmp_step=1+steps(tunnel[0],target,visited)
            visited=visited[0:visit]
            if tmp_step < min_step:
                min_step=tmp_step
    return min_step
        
 
def prioritise(position,time):
    valve_priority={}
    for valve in valves:
        if not valve.isopen and valve.flow > 0 and valve != position:
            togo=distance[position.name+valve.name]
            if time-togo-1<0:
                continue
            act_priority=(valve.flow*(time-togo-1)/togo)
            valve_priority[act_priority]=valve
    return valve_priority

def choose(cur,next,time):
    togo=distance[cur.name+next.name]
    best=0
    cur_time=time-togo-1
    next.isopen=True
    if cur_time < 0:
        return 0
    prio=prioritise(next,cur_time)
    for key in sorted(prio.keys(),reverse=True):
        node=prio[key]
        tmp=choose(next,node,cur_time)
        node.isopen=False
        if tmp > best:
            best=tmp
    return best+next.flow*(cur_time)

def create_path(cur_path,node,time):
    poss=prioritise(node,time)
    tmp_path=cur_path+[node]
    node.isopen=True
    for key in poss.keys():
        node2=poss[key]
        togo=distance[node.name+node2.name]
        create_path(tmp_path,node2,time-togo-1)
        node2.isopen=False
    paths.append(tmp_path)

def evaluate_path(path,time):
    pressure=0
    cur=starting_valve
    for i in range(0,len(path)):
        next=path[i]
        cost=distance[cur.name+next.name]+1
        time=time-cost
        pressure+=next.flow*time
        cur=next
    return pressure

valves=[]

with open(sys.argv[1],"r") as f:
    lines=f.readlines()
connections=[[] for _ in range(0,len(lines))]

start="AA"

# Read the Input
for i in range(0,len(lines)):
    line=lines[i].translate({ord(x): None for x in ";,"}).split()
    valves.append(valve(line[1],int(line[4].split("=")[1])))
    if valves[i].name==start:
        starting_valve=valves[i]
    for x in range(9,len(line)):
        connections[i].append(line[x])

# Connect Valves
for i in range(0,len(valves)):
    for tunnel in connections[i]:
        try:
            valves[i].connections.append([v for v in valves if tunnel in v.name])
        except:
            print("Could not find connection "+str(tunnel))
            sys.exit()

released_pressure=0
time=30

cur=starting_valve

distance={}
for node in valves:
    for node2 in valves:
        if node.name+node2.name not in distance.keys() and node.flow > 0 and node2.flow > 0 or node == starting_valve:
            distance[node.name+node2.name]=steps(node,node2,[])
            distance[node2.name+node.name]=distance[node.name+node2.name]

prio=prioritise(cur,time)
for key in sorted(prio.keys(),reverse=True):
    next_valve=prio[key]
    for i in range(0,len(valves)):
        valves[i].isopen=False
    tmp_release=choose(cur,next_valve,time)
    if tmp_release > released_pressure:
        released_pressure=tmp_release


print("I can release: "+str(released_pressure)+" pressure.")
print()
print("Let's teach an elephant!")
# Create all possible paths
poss=prioritise(cur,time)
paths=[]
time=30
for valve in valves:
    valve.isopen=False
print()
print("Making a map of all possible paths...")
for key in tqdm(poss.keys()):
    node=poss[key]
    tmp_path=[]
    togo=distance[cur.name+node.name]
    create_path(tmp_path,node,time-togo-1)
    node.isopen=False

best=0
time=26

#Give every path a value and delete inefficient paths (Brute Force takes > 6 hours :( )
values={}
print("Feeding the elephant to gain its trust...")
for path in tqdm(paths):
    value=evaluate_path(path,time)
    string_key=" ".join([x.name for x in path])
    string_key=" ".join(sorted(string_key.split(" ")))
    if string_key in values.keys():
        if value > values[string_key]:
            values[string_key]=value
    else:
        values[string_key]=value

print("Teaching the elephant... Good luck!")

#Add the best two pathes that don't overlap
for key in tqdm(values.keys()):
    for key2 in values.keys():
        if not any(i in key.split(" ") for i in key2.split(" ")):   
            tmp=values[key]+values[key2]
            if tmp > best:
                best=tmp
print()
print("The elephant bumps this to: "+str(best)+".")
print()


