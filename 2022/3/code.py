# Advent of code Year 2022 Day 3 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022
# autism-inducing code; don't read it!!!

import string

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    pri_c = 0
    alph = string.ascii_lowercase + string.ascii_uppercase
    values = dict()
    overlap = ''

    for index, letter in enumerate(alph):
        values[letter] = index + 1

    for x in input:
        line1 = set(x[0:len(x)//2]) 
        line2 = set(x[len(x)//2:len(x)]) 
        overlap += line1.intersection(line2).pop()

    overlap = ''.join(overlap)                

    for y in overlap:
        pri_c += values[y]
   
    input2 = [entry.strip() for entry in input]
    rucksack_sum = 0
    while len(input2) > 0:
        first_rucksack = set(input2.pop())
        second_rucksack = set(input2.pop())
        third_rucksack = set(input2.pop())
        overlap_char = ((first_rucksack.intersection(second_rucksack)).intersection(third_rucksack)).pop()
        
        overlap_char = ''.join(overlap_char)

        for y in overlap_char:
            rucksack_sum += values[y]

print("Part One: "+ str(pri_c))
print("Part Two: "+ str(rucksack_sum))
