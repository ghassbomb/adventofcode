# Advent of code Year 2022 Day 1 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    calories = [x.rstrip('\n') for x in input]
    cals = 0
    totalcal = []
    for x in calories:
        if x == '':
            totalcal.append(cals)
            cals = 0
            continue
        cals += int(x)
    totalcal.sort(reverse=True)

print("Part One : "+ str(totalcal[0]))
print("Part Two : "+ str(totalcal[0] + totalcal[1] + totalcal[2]))
