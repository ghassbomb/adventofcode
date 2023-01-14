#l Advent of code Year 2022 Day 8 solution
# Author = Ghassan Shahzad (fr06t)
# Date = December 2022


class TreeGrid: 
    def __init__(self, block):
        self.grid = []
        xline = []
        for line in block:
            if line == '':
                self.grid.append(xline)
                xline = []
                continue
            xline.append(int(line))


    def is_visible(self, x, y):
        # If at-edge, then True
        if x == 0 or y == 0 or x == len(self.grid[x])-1 or y == len(self.grid[y])-1:
            print("at-edge")
            return True
        # Is visible from right?
        for char in range(y+1, len(self.grid[x])):
            if self.grid[x][y] > self.grid[x][char]:
                if char == len(self.grid[x])-1:
                    print("r")
                    return True
            else:
                break

        # Is visible from left?
        for char in range(y):
            if self.grid[x][y] > self.grid[x][char]:
                if char == y-1:
                    print("l")
                    return True
            else:
                break

        # Is visible from top?
        for char in range(0, x, -1):
            if self.grid[x][y] > self.grid[char][y]:
                if char != x-1:
                    print("t")
                    return True
            else:
                break

       # Is visible from bottom?
        for char in range(x+1, len(self.grid[y])):
            if self.grid[x][y] > self.grid[char][y]:
                if char == len(self.grid[y])-1:
                    print("b")
                    return True
            else:
                break


        return False

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [s.strip('\n') for s in input_file.read()]
    grid = TreeGrid(input)
    counter = 0
    for x in range(len(grid.grid)):
        for y in range(len(grid.grid[x])):
            if grid.is_visible(int(x),int(y)):
                counter += 1



print("Part One : "+ str(counter))
print("Part Two : "+ str(None))
