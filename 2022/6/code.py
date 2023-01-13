# Advent of code Year 2022 Day 6 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

def find_pack_marker(input):
    char_count = 0
    for char in range(len(input[0])):
        breaker = True
        char_count += 1
        comp = [input[0][char+x] for x in range(4)]

        for elem in comp:
            if comp.count(elem) > 1:
                breaker = False
                break
        if breaker:
            return char_count + 3

def find_msg_marker(input):
    char_count = 0
    for char in range(len(input[0])):
        breaker = True
        comp = [input[0][char+x] for x in range(4)]
        char_count += 1
        
        for elem in comp:
            if comp.count(elem) > 1:
                breaker = False
                break

        if breaker:
            return char_count + 13 

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

print("Part One : ", find_pack_marker(input))
print("Part Two : ", find_msg_marker(input))
