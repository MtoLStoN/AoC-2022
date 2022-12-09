#!/bin/python3

import sys

def getsize(directory):
    tempsize=0
    for j in fs:
        if directory in j:
            tempsize+=fs[j]
    return tempsize

fs = {}
limit=100000
filesystemsize=70000000
updatesize=30000000
try:
    f = open(str(sys.argv[1]),'r')
except:
    print('Could not open file "'+str(sys.argv[1])+'".')
    exit()
lines = f.readlines()
wd = []

for i in range(0,len(lines)):
    command=lines[i].strip().split(" ")
    if command[0] != "$":
        continue
    if command[1] == "cd":
        if command[2] == "..":
            wd.pop()
        else:
            wd.append(command[2])
    if command[1] == "ls":
        temp_size=0
        for j in range(i+1,len(lines)):
            ls=lines[j].strip().split(" ")
            if ls[0] == "$":
                fs["/".join(wd)] = temp_size
                break
            elif ls[0] == "dir":
                continue
            else:
                temp_size+=int(ls[0])
            if j == len(lines)-1:
                fs["/".join(wd)] = temp_size
                break

size=0
for i in fs:
    current_size=getsize(i)
    if current_size < limit:
        size=size+current_size
print(size)

needed=updatesize-(filesystemsize-getsize(""))
smallest=filesystemsize
for i in fs:
    current_size=getsize(i)
    if current_size > needed and current_size < smallest:
        smallest=current_size
print(smallest)
