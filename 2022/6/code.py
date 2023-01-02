# Advent of code Year 2022 Day 6 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

def find_pack_marker(input):
    char_count = 0
    for char in range(len(input[0])):
        breaker = True
        comp = [] # List to store next 4 char in
        char_count += 1 # Counter

        for x in range(4):
            # Loop to store next 4 char in comp
            comp += input[0][char+x]

        for elem in comp:
            if comp.count(elem) > 1:
                breaker = False
                break
         
        if breaker == True:
            return char_count + 3

def find_msg_marker(input):
    char_count = 0
    for char in range(len(input[0])):
        breaker = True
        comp = [] # List to store next 4 char in
        char_count += 1 # Counter

        for x in range(14):
            # Loop to store next 4 char in comp
            comp += input[0][char+x]

        for elem in comp:
            if comp.count(elem) > 1:
                breaker = False
                break
         
        if breaker == True:
            return char_count + 13 

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

print("Part One : "+ str(find_pack_marker(input)))
print("Part Two : "+ str(find_msg_marker(input)))
