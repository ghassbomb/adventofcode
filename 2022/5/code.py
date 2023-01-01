# Advent of code Year 2022 Day 5 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

import string

class Stack:
    def __init__(self, index):
        self.index = index
        self.crates = []

    def add_crate(self, crate): # Goes top --> bottom
        self.crates.append(crate)
        
    def move_crate(self, dest):
        dest.crates.insert(0, self.crates.pop(0))

    def move_crate_9001(self, dest, num):
        for x in reversed(range(num)):
            print(self.crates, dest.crates, x)
            dest.crates.insert(0, self.crates.pop(x))

    def top_crate(self):
        return self.crates[0]

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    
    sol = ''
    stack_num = len(input[0]) // 4 
    stacks = [Stack(x) for x in range(stack_num)]
    
    for line in input:
        for char in range(len(line)):
            if line[char] in string.ascii_uppercase:
                x = (((char-1)//2)//2)
                stacks[x].add_crate(line[char])
    """
    # PART 1
    for line in input:
        if input.index(line) >= 10:
            vars = [int(s) for s in line.split() if s.isdigit()]
            for x in range(vars[0]):
                stacks[vars[1]-1].move_crate(stacks[vars[2]-1])



    for stack in stacks:
        sol += stack.top_crate()
    """
    for line in input:
        if input.index(line) >= 10:
            vars = [int(s) for s in line.split() if s.isdigit()]
            stacks[vars[1]-1].move_crate_9001(stacks[vars[2]-1], vars[0])
    
    sol2 = ''

    for stack in stacks:
        sol2 += stack.top_crate()

print("Part One : "+ str(sol))
print("Part Two : "+ str(sol2))
