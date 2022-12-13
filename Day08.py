import pandas as pd
import numpy as np

# # Load
# with open("input8b.txt", "r") as file:
#     a = [[int(x) for x in line.split()] for line in file]



# with open('input8b.txt') as my_file:
#     a = my_file.readlines()


a = []

f = open('input8.txt')

for line in f:
    a.append(line.rstrip('\n'))

f.close()




print(a)
# 30373
# 25512
# 65332
# 33549
# 35390


def split_str(s):
    return [c for c in s]


grid = []

# Print
for x in a: 
    aa = str(x)
    t = split_str(aa)
    grid.append(t)

print(grid)

for  x in range(0,len(grid)):
    print(''.join(grid[x]))

print(f'height = {len(grid)}')
print(f'length = {len(grid[0])}')

variable = input('input something!: ')

height = len(grid)
length = len(grid[0])

visiblecount = 0
for i in range(height) : 
    for j in range(length) :
        visflag = 0
        print(f'coordinates: {i} {j} have the value: {grid[i][j]}') 
        # is border? ( a border has at least one coord i = 0  or i = height -1   or j = 0 or j = length -1 ) value doesn't matter
        if (i == 0 or i == height -1 or j == 0 or j == length -1):
            print('border')
            visflag = 1
            # visiblecount += 1

            # break
        # is visible N? the current value is grid[i][j] say 1,1 = 5,  are all values 0,1 ( current j to 0 ) less than 5
        if visflag == 0:
            visflag = 1
            isblockedN = False
            for x in range (0,i ):
                print(f'northtest {x} {j}: {grid[x][j]} ')
                if grid[i][j] <= grid[x][j]:
                    # print('blocked')
                    isblockedN = True
            
        # is visible S
            isblockedS = False
            for x in range (i+1,height ):
                print(f'Southtest {x} {j}: {grid[x][j]} ')
                if grid[i][j] <= grid[x][j]:
                    # print('blocked')
                    isblockedS = True
        # is visible W
            isblockedW = False
            for x in range (0,j ):
                print(f'Westtest {i} {x}: {grid[i][x]} ')
                if grid[i][j] <= grid[i][x]:
                    # print('blocked')
                    isblockedW = True
        # is visible E
            isblockedE = False
            for x in range (j+1,length ):
                print(f'Easttest {i} {x}: {grid[i][x]} ')
                if grid[i][j] <= grid[i][x]:
                    # print('blocked')
                    isblockedE = True
            if(isblockedN and isblockedS and isblockedW and isblockedE):
                visflag = 0

        if visflag == 1:
            visiblecount += 1
     

print(f'The Visible Count is: {visiblecount}')

# # look()

# def look(direction, x,y):
#     print(direction)
#     return 1

variable = input('input something!: ')
