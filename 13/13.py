#!/bin/python3
import sys
from ast import literal_eval

def right_order(package1,package2):
    for i in range(0,max(len(package1),len(package2))):
        try:
            left=package1[i]
        except:
            return True
        if isinstance(left,int):
            try:
                right=package2[i]
            except:
                return False
            if isinstance(right,int):
                if left < right:
                    return True
                elif left > right:
                    return False
                else:
                    continue
            else:
                if right_order([left],right) is not None:
                    return right_order([left],right)
                else: 
                    continue
        else:
            try:
                right=package2[i]
            except:
                return False
            if isinstance(right,int): 
                if right_order(left,[right]) is not None:
                    return right_order(left,[right])
                else: 
                    continue
            else:
                if right_order(left,right) is not None:
                    return right_order(left,right)
                else:
                    continue
    return None


with open(sys.argv[1],"r") as f:
    packages = list(map(literal_eval, [l for l in f if l.strip()]))

sum=0

i=0
index=1
while i<len(packages):
    if right_order(packages[i],packages[i+1]):
        sum+=index
    i+=2
    index+=1

print(sum)

packages.append([[2]])
packages.append([[6]])

i=0
#This should be a better sorting algorithm but I only know bubble sort.
swapped=True
while swapped:
    swapped=False
    for i in range(0,len(packages)-1):
        if not right_order(packages[i],packages[i+1]):
            tmp_package=packages[i]
            packages[i]=packages[i+1]
            packages[i+1]=tmp_package
            swapped=True

sum=1

for i in range(0,len(packages)):
    if packages[i] == [[2]]:
        sum*=i+1
    if packages[i] == [[6]]:
        sum*=i+1

print(sum)
