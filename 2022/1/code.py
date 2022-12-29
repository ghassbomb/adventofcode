# Advent of code Year 2022 Day 1 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    most_cal = 0
    total_cal = 0
    secondmost_cal = 0 
    thirdmost_cal = 0
    ttotal_cal = 0
    for line in input:
        if line.strip():
           total_cal += int(line) 
        else:
            if total_cal > most_cal:
                secondmost_cal = most_cal
                most_cal = total_cal
            elif total_cal > secondmost_cal:
                thirdmost_cal = secondmost_cal
                secondmost_cal = total_cal
            elif total_cal > thirdmost_cal:
                thirdmost_cal = total_cal
            total_cal = 0
    ttotal_cal = most_cal + secondmost_cal + thirdmost_cal

print("Part One : "+ str(most_cal))
print("Part Two : "+ str(ttotal_cal))
