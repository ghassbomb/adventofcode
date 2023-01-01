# Advent of code Year 2022 Day 4 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    count = 0
    ocount = 0
    for line in input:
        firstelf_range = []
        secondelf_range = []
        firstelf = ""
        secondelf = ""
        for char in range(len(line)):
            if line[char] == ',':
                firstelf = line[:char]
                secondelf = line[char+1:]
        for num in range(int(firstelf[:firstelf.find('-')]), int(firstelf[firstelf.find('-')+1:])+1):
            firstelf_range.append(num) 
        for num in range(int(secondelf[:secondelf.find('-')]), int(secondelf[secondelf.find('-')+1:])+1):
            secondelf_range.append(num) 
        if set(firstelf_range).issubset(set(secondelf_range)) or set(secondelf_range).issubset(set(firstelf_range)):
            count += 1
        if set(firstelf_range).intersection(set(secondelf_range)) or set(secondelf_range).intersection(set(firstelf_range)):
            ocount += 1
print("Part One : "+ str(count))
print("Part Two : "+ str(ocount))
