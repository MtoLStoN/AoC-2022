#!/bin/python3

import copy

print("Which file?")
fileinput= input()

f = open(fileinput,'r')
lines = f.readlines()

setup = []
plan = []

for i in range(0,len(lines)):
    if not lines[i].strip():
        setup=lines[:i]
        plan=lines[i+1:]
        break

stacks=int(setup[len(setup)-1].split()[len(setup[len(setup)-1].split())-1])
setup.pop(len(setup)-1)

Stack =  [[] for _ in range(0,stacks)]

for i in range(0,len(setup)):
    stack_number=len(setup)-i-1
    for j in range(0,stacks):
        if list(setup[stack_number])[1+4*j].strip(): 
            Stack[j].append(list(setup[stack_number])[1+4*j])

Stack_9001=copy.deepcopy(Stack)

for command in plan:
    move_amount=int(command.split()[1])
    move_from=int(command.split()[3])
    move_to=int(command.split()[5])

    #Cranemover 9000
    for i in range(0,move_amount):
        Stack[move_to-1].append(Stack[move_from-1].pop())

    #Cranemover 9001
    tmp_list=Stack_9001[move_from-1][-move_amount:]
    for test in tmp_list:
        Stack_9001[move_to-1].append(test)
    Stack_9001[move_from-1]=Stack_9001[move_from-1][:-move_amount]

answer=''
answer_9001=''

for i in range(0,stacks):
    answer=answer+Stack[i][-1]
    answer_9001=answer_9001+Stack_9001[i][-1]

print("Cranemover 9000: "+answer)
print("Cranemover 9001: "+answer_9001)

f.close()
