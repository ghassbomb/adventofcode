# Advent of code Year 2022 Day 4 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

def numrange(s):
    line1 = s[:s.find(',')].strip(',')
    line2 = s[s.find(','):].strip(',')
    return [x for x in range(int(line1[:line1.find('-')]), int(line1[line1.find('-')+1:])+1)], [x for x in range(int(line2[:line2.find('-')]), int(line2[line2.find('-')+1:])+1)]

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    count = 0
    ocount = 0
    for line in input:
        firstelf_range, secondelf_range = numrange(line)
        if set(firstelf_range).issubset(set(secondelf_range)) or set(secondelf_range).issubset(set(firstelf_range)):
            count += 1
        if set(firstelf_range).intersection(set(secondelf_range)) or set(secondelf_range).intersection(set(firstelf_range)):
            ocount += 1

print("Part One : "+ str(count))
print("Part Two : "+ str(ocount))
