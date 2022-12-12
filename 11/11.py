#!/bin/python3
import sys

class monkey():
    def __init__(self, starting_items, operator, operation, test):
        self.items = starting_items
        self.operator = operator
        self.operation = operation
        self.test = test
        self.inspector=0
    def inspect(self,bored):
        for item in range(0,len(self.items)):
            self.inspector+=1
            self.items[item]%=scd
            if self.operator=="+":
                self.items[item]+=self.operation
            elif self.operator=="-":
                self.items[item]-=self.operation
            elif self.operator=="*":
                self.items[item]*=self.operation
            elif self.operator=="/":
                self.items[item]//=self.operation
            elif self.operator=="**":
                self.items[item]**=self.operation
            if bored:
                self.items[item]//=3

lines = open(file=sys.argv[1], mode='r').readlines()

monkeys = []
items = []

scd=1

for i in range(0,len(lines)):
    if "Monkey" in lines[i]:
        items = [int(x) for x in lines[i+1].replace(",","").split()[2:]]
        if lines[i+2].split()[5] == "old":
            operator="**"
            operation=2
        else:
            operator=str(lines[i+2].split()[4])
            operation=int(lines[i+2].split()[5])
        test = [int(lines[i+3].split()[3]), int(lines[i+4].split()[5]), int(lines[i+5].split()[5])]
        scd *= test[0]
        monkeys.append(monkey(items, operator, operation, test))

for round in range(0,10000):
    for turn in range(0,len(monkeys)):
        monkeys[turn].inspect(False)
        for item in range(0,len(monkeys[turn].items)):
            if (monkeys[turn].items[item]%monkeys[turn].test[0]) == 0:
                monkeys[monkeys[turn].test[1]].items.append(monkeys[turn].items[item])
            else:
                monkeys[monkeys[turn].test[2]].items.append(monkeys[turn].items[item])
        monkeys[turn].items = []

monkey_inspection = []
for i in range(0,len(monkeys)):
    print("Monkey "+str(i+1)+": "+str(monkeys[i].inspector))
    monkey_inspection.append(monkeys[i].inspector)
monkey_inspection.sort(reverse=True)
print(monkey_inspection[0]*monkey_inspection[1])