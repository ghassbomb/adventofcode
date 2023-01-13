# Advent of code Year 2022 Day 3 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

import string

def common(s):
    line1 = s[:len(s)//2].strip()
    line2 = s[len(s)//2:].strip()
    return [*set([x for x in line1 if x in line2])]

def three_common(s1, s2, s3):
    return [*set([x for x in s1 if x in s2 and x in s3])]

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    # Part 1
    indices = string.ascii_lowercase + string.ascii_uppercase
    common_letters = [item for sublist in [common(x) for x in input] for item in sublist]
    values = [indices.find(x)+1 for x in common_letters]

    # Part 2
    common_group_letters = [item for sublist in [three_common(input[x], input[x+1], input[x+2]) for x in range(0, len(input), 3)] for item in sublist]
    values2 = [indices.find(x)+1 for x in common_group_letters]

print("Part One: "+ str(sum(values)))
print("Part Two: "+ str(sum(values2)))
