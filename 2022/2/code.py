# Advent of code Year 2022 Day 2 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    score = 0
    tscore = 0
    for line in input:
        if line[0] == "A" and line[2] == "X":
            score += 3+1
            tscore += 0+3
        if line[0] == "A" and line[2] == "Y":
            score += 6+2
            tscore += 3+1
        if line[0] == "A" and line[2] == "Z":
            score += 0+3
            tscore += 6+2
        if line[0] == "B" and line[2] == "X":
            score += 0+1
            tscore += 0+1
        if line[0] == "B" and line[2] == "Y":
            score += 3+2
            tscore += 3+2
        if line[0] == "B" and line[2] == "Z":
            score += 6+3
            tscore += 6+3
        if line[0] == "C" and line[2] == "X":
            score += 6+1
            tscore += 0+2
        if line[0] == "C" and line[2] == "Y":
            score += 0+2
            tscore += 3+3
        if line[0] == "C" and line[2] == "Z":
            score += 3+3
            tscore += 6+1

    


print("Part One : "+ str(score))
print("Part Two : "+ str(tscore))
