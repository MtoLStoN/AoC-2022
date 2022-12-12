#!/bin/python3

import sys

argument=str(sys.argv[1])

f = open(argument, "r")
lines = f.readlines()

X=1
cycle=0
X_cycle=[]

for line in lines:
    if "noop" in line:
        cycle=cycle+1
        X_cycle.append(X)
    elif "addx" in line:
        X_cycle.append(X)
        X=X+int(line.split(" ")[1])
        cycle=cycle+2
        X_cycle.append(X)

signal_strenght=[]
for i in range(0,len(X_cycle)):
    signal_strenght.append(X_cycle[i]*(i+2))

print(signal_strenght[18]+signal_strenght[58]+signal_strenght[98]+signal_strenght[138]+signal_strenght[178]+signal_strenght[218])

X_cycle.insert(0,1)
part_line=""
for part in range(0,6):
    for cycle in range(0,40):
        if X_cycle[(part*40)+cycle] in range(cycle-1,cycle+2):
            part_line=part_line+"#"
        else:
            part_line=part_line+"."
    print(part_line)
    part_line=""