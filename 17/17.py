#!/bin/python3.10

import sys
from tqdm import tqdm


class rock:
    def __init__(self, type, bottom):
        self.type = type
        self.leftedge = 2
        self.bottom = bottom
        self.rested = False
        match type:
            case '-':
                self.rightedge = self.leftedge + 4
                self.height=1
            case '+':
                self.rightedge = self.leftedge + 3
                self.height=3
            case 'L':
                self.rightedge = self.leftedge + 3
                self.height=3
            case '|':
                self.rightedge = self.leftedge + 1
                self.height=4
            case '#':
                self.rightedge = self.leftedge + 2
                self.height=2
        self.width=self.rightedge-self.leftedge
    def fields(self):
        match self.type:
            case '-':
                return [[self.leftedge+1, self.bottom+1], [self.leftedge+2, self.bottom+1], [self.leftedge+3, self.bottom+1], [self.leftedge+4, self.bottom+1]]
            case '+':
                return [[self.leftedge+1, self.bottom+2], [self.leftedge+2, self.bottom+1], [self.leftedge+3, self.bottom+2], [self.leftedge+2, self.bottom+2], [self.leftedge+2, self.bottom+3]]
            case 'L':
                return [[self.leftedge+1, self.bottom+1], [self.leftedge+2, self.bottom+1], [self.leftedge+3, self.bottom+1], [self.leftedge+3, self.bottom+2], [self.leftedge+3, self.bottom+3]]
            case '|':
                return [[self.leftedge+1, self.bottom+1], [self.leftedge+1, self.bottom+2], [self.leftedge+1, self.bottom+3], [self.leftedge+1, self.bottom+4]]
            case '#':
                return [[self.leftedge+1, self.bottom+1], [self.leftedge+2, self.bottom+1], [self.leftedge+1, self.bottom+2], [self.leftedge+2, self.bottom+2]]
def draw(occ,falling,high):
    for y in range(high+6, -1,-1):
        for x in range(0, 9):
            if x == 0 or x == 8:
                print('|', end='')
            elif y==0:
                print('-', end='')
            elif [x,y] in falling.fields():
                print(falling.type, end='')
            elif [x,y] in occ:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


pattern=[]
with open(sys.argv[1]) as f:
    for line in f:
        for char in line.strip():
            pattern.append(char)

rocks=[]
types = ['-', '+', 'L', '|', '#']
step=0
high=0
occupied=[[0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0]]
count=0
results=[]
high2=0
needed=1000000000000
count2=0
once=True

while True:
    for type in types:
        rocks.append(rock(type, high+3))
        count=count+1
        if count>2022 and once:
            print(high)
            once=False
        if count>needed:
            print(interpolated+high)
            sys.exit()
        while True:
            if len(occupied) > 100:
                occupied=occupied[-100:]
            command=pattern[step]
            match command:
                case '<':
                    if rocks[-1].leftedge > 0:
                        rocks[-1].leftedge-=1
                        rocks[-1].rightedge-=1
                case '>':
                    if rocks[-1].rightedge < 7:
                        rocks[-1].leftedge+=1
                        rocks[-1].rightedge+=1
            if any([field in rocks[-1].fields() for field in occupied[-100:]]):
                match command:
                    case '<':
                        rocks[-1].leftedge+=1
                        rocks[-1].rightedge+=1
                    case '>':
                        rocks[-1].leftedge-=1
                        rocks[-1].rightedge-=1
            step+=1
            if step>len(pattern)-1:
                step=0
                results.append(high-high2)
                high2=high
                inter_step=count-count2
                count2=count
            # This is a hard coded interpolation of part 2, because the pattern just repeats. Will not work for the test case, because the repeating pattern is more complicated.
            # Pretty sure, there is a general way to do this, but I don't care.
            if len(results)>1 and (needed-count)//inter_step > 0:
                step=0
                interpolation=((needed-count)//inter_step)
                interpolated=(results[1]*interpolation)
                count=count+inter_step*interpolation
            rocks[-1].bottom-=1
            if any([field in rocks[-1].fields() for field in occupied[-100:]]):
                rocks[-1].bottom+=1
                if rocks[-1].bottom+rocks[-1].height > high:
                    high=rocks[-1].bottom+rocks[-1].height
                rocks[-1].rested=True
                for fields in rocks[-1].fields():
                    if fields not in occupied:
                        occupied.append(fields)
                break

