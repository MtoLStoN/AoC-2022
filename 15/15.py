#!/bin/python3

import sys

class sensor:
    def __init__(self, position, beacon):
        self.position=position
        self.beacon=beacon
        self.distance=abs(beacon[0]-position[0])+abs(beacon[1]-position[1])


def scan(circle):
    for position in circle:
        x=position[0]
        y=position[1]
        Possible=True
        for s in sensors:
            if s.distance >= abs(s.position[0]-x)+abs(s.position[1]-y):
                Possible=False
                break
        if Possible:
            print("\n"+"Tuning Frequency: "+str(x*4000000+y))
            sys.exit()

with open(sys.argv[1]) as f:
    lines=f.readlines()

sensors=[]
width=[0,0]

for line in lines:
    line=line.strip().translate({ord(c): None for c in ',:xy='}).split()
    sx,sy=int(line[2]),int(line[3])
    bx,by=int(line[8]),int(line[9])
    sensors.append(sensor((sx,sy),(bx,by)))
    if len(sensors) == 1:
        width[0]=sx-sensors[-1].distance
        width[1]=sx+sensors[-1].distance
    if sx-sensors[-1].distance<width[0]:
        width[0]=sx-sensors[-1].distance
    if sx+sensors[-1].distance>width[1]:
        width[1]=sx+sensors[-1].distance

y=2000000
count=0
for x in range(width[0],width[1]+1):
    for s in sensors:
        if s.distance >= abs(s.position[0]-x)+abs(s.position[1]-y):
            count=count+1
            break
    for s in sensors:
        if s.beacon[0]==x and s.beacon[1]==y: 
            count=count-1
            break
    print("Scanning: "+str(x),end="\r")
print("\n"+str(count))

circle=[]
width=[0,4000000]
#Only one possible beacon location means that the beacon is just outside the range of the sensors
for s in sensors:
    for diffx in range(0,s.distance+1):
        diffy=s.distance+1-diffx
        x=s.position[0]+diffx
        y=s.position[1]+diffy
        if x in range(width[0],width[1]+1) and y in range(width[0],width[1]+1):
            circle.append([x,y])
print("Number of possible beacon locations :" +str(len(circle)))
scan(circle)