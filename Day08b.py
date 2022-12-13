import pandas as pd
import numpy as np

# part 2 of day 8.  Calculate scenic Score

print('Day 8 Part2')
print('')

# load in the data:
a = []
f = open('input8.txt')
for line in f:
    a.append(line.rstrip('\n'))
f.close()


# Check loaded data 1
print('Array Of Lines:')
print(a)
print('')

# function to split each line
def split_str(s):
    return [c for c in s]

# split each line into a list.
grid = []
# Print
for x in a: 
    aa = str(x)
    t = split_str(aa)
    grid.append(t)

print('Split Array. Multi List')
print(grid)

print('Joined:')
for  x in range(0,len(grid)):
    print(''.join(grid[x]))

print(f'height = {len(grid)}')
print(f'length = {len(grid[0])}')

variable = input('input something!: ')

height = len(grid)
length = len(grid[0])


MaxScore = 0
visiblecount = 0
for i in range(height) : 
    for j in range(length) :
        visflag = 0
        Nvis = 0
        Evis = 0
        Svis = 0
        Wvis = 0
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
            for x in reversed(range (0,i )):
                print(f'northtest {x} {j}: {grid[x][j]} ')
                if grid[i][j] <= grid[x][j]:
                    # print('blocked')
                    isblockedN = True
                    Nvis += 1
                    break
                else:
                    Nvis += 1
            
        # is visible S
            isblockedS = False
            for x in range (i+1,height ):
                print(f'Southtest {x} {j}: {grid[x][j]} ')
                if grid[i][j] <= grid[x][j]:
                    # print('blocked')
                    isblockedS = True
                    Svis += 1
                    break
                else:
                    Svis += 1
        # is visible W
            isblockedW = False
            for x in reversed(range (0,j )):
                print(f'Westtest {i} {x}: {grid[i][x]} ')
                if grid[i][j] <= grid[i][x]:
                    # print('blocked')
                    isblockedW = True
                    Wvis += 1
                    break
                else:
                    Wvis += 1
        # is visible E
            isblockedE = False
            for x in range (j+1,length ):
                print(f'Easttest {i} {x}: {grid[i][x]} ')
                if grid[i][j] <= grid[i][x]:
                    # print('blocked')
                    isblockedE = True
                    Evis += 1
                    break
                else:
                    Evis += 1
            if(isblockedN and isblockedS and isblockedW and isblockedE):
                visflag = 0

        if visflag == 1:
            visiblecount += 1
        print(f'VisScore: N{Nvis},E{Evis},S{Svis},W{Wvis} Score = {Nvis*Evis*Svis*Wvis}')
        if (Nvis*Evis*Svis*Wvis > MaxScore):
            MaxScore = Nvis*Evis*Svis*Wvis
     

print(f'The Visible Count is: {visiblecount} The MaxScore is {MaxScore}')

# # look()

# def look(direction, x,y):
#     print(direction)
#     return 1

variable = input('input something!: ')
