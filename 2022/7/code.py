# Advent of code Year 2022 Day 7 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022
from collections import defaultdict

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    
    sizes = defaultdict(int)
    stack = []

    i = 0
    for c in input:
        if c.startswith("$ ls") or c.startswith("dir"):
            continue
        if c.startswith("$ cd"):
            dest = c.split()[2]
            if dest == "..":
                stack.pop()
            else:
                i += 1
                path = f"{stack[-1]}_{dest}" if stack else dest
                stack.append(path)
        else:
            size, file = c.split()
            for path in stack:
                sizes[path] += int(size)

    needed_size = 30000000 - (70000000 - sizes["/"])
    for size in sorted(sizes.values()):
        if size > needed_size:
            break
print("Part One : "+ str(sum(n for n in sizes.values() if n <= 100000)))
print("Part Two : "+ str(size))
