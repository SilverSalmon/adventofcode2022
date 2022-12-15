import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# Day 10


df = pd.read_csv("input10.txt",delimiter = ' ', engine='python' , header=None)

df.columns = ['com','val']


print(df)
# [xval, comprocess]
cyclesTracker= []
reg = 1
valatnextcyc = 0
for ind in df.index:
    if valatnextcyc != 0:
        reg = reg + valatnextcyc
    valatnextcyc = 0
    # print(df['com'][ind], df['val'][ind])
    if df['com'][ind] == 'noop':
        cyclesTracker.append([reg,'noop'])
    if df['com'][ind] == 'addx':
        cyclesTracker.append([reg,df['val'][ind]])
        cyclesTracker.append([reg,df['val'][ind]])
        valatnextcyc = df['val'][ind]

summer = 0
for x in range(0,len(cyclesTracker)):
    if x in([20-1,60-1,100-1,140-1,180-1,220-1]):
        print(f'cyc:{x+1} regx:{cyclesTracker[x][0]} curcom:{cyclesTracker[x][1]} cycstrength: {(x+1) * cyclesTracker[x][0]  }')
        summer += (x+1) * cyclesTracker[x][0] 

print(f'The total is:{summer}')

print('  ')

#  part 2

line =  ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
line1 = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
line2 = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
line3 = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
line4 = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
line5 = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']


screen =[]

screen.append(line)
screen.append(line1)
screen.append(line2)
screen.append(line3)
screen.append(line4)
screen.append(line5)


def drawpix(cyc):
    # print('cyc')
    if  1 <= cyc <= 40:
        screen[0][cyc-1] = '#'
    if 41 <= cyc <= 80: 
        screen[1][cyc-1 -40] = '#'
    if 81 <= cyc <= 120:
        screen[2][cyc-1 -80] = '#'
    if 121 <= cyc <= 160:
        screen[3][cyc-1 -120] = '#'
    if 161 <= cyc <= 200:
        screen[4][cyc-1 -160] = '#'
    if 201 <= cyc <= 240:
        screen[5][cyc-1 -200] = '#'







part2 = []
for x in range(0,len(cyclesTracker)):
    # if x in([20-1,60-1,100-1,140-1,180-1,220-1]):
        # print(f'cyc:{x+1} regx:{cyclesTracker[x][0]} curcom:{cyclesTracker[x][1]} cycstrength: {(x+1) * cyclesTracker[x][0]  }')
        part2.append([x+1,cyclesTracker[x][0],cyclesTracker[x][1]])

print(part2)


sprite = [1,2,3]

def movesprite(middle):
    sprite = [middle -1, middle, middle +1]
    return sprite

count =0
for x in part2:
    # is the sprite at the cyle?
    # move the sprite.
    sprite = movesprite(x[1] +1)
    print(f'sprite:{sprite}')
    print(f'start cycle:{x[0]} begin exec {x[2]}')
    print(f'during cycle:{x[0]} Crt draws at pos {x[0] -1}')
    print(x[0]%40)
    if x[0]%40 in sprite:
        
        drawpix(x[0])
    
    # for x in screen:
    #     print("".join(x))
    count += 1
    # input()
    # if count > 5:
    #     break
    



# z = input()




for x in screen:
    print("".join(x))


input()