import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# Day 9



# Read in data

df1 = pd.read_csv("input9c.txt",delimiter = ' ', engine='python' , header=None)
df1.columns =  ['direction', 'steps']
    
print(df1)

# Rules of motion


Hloc= [0,0]
Tloc= [0,0]
Hlochistory = [[0,0]]
Tlochistory = [[0,0]]

# Get Header history in an array.
for idx, row in df1.iterrows():
    # print(f'move {row.direction} {row.steps} steps')
    if(row.direction == 'R'):
        # print(f'Move R {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0] +1 , Hloc[1]]
            Hlochistory.append(Hloc)
    if(row.direction == 'L'):
        # print(f'Move L {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0]  -1 , Hloc[1]]
            Hlochistory.append(Hloc)
    if(row.direction == 'U'):
        # print(f'Move U {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0] , Hloc[1] +1]
            Hlochistory.append(Hloc)
    if(row.direction == 'D'):
        # print(f'Move D {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0] , Hloc[1] -1]
            Hlochistory.append(Hloc)



def generateHistory(Hlochistory):
    Tlochistory = [[0,0]]
    loc = 0
    for x in Hlochistory:
        print(f'H is at {x}. T is at {Tlochistory[-1]}')
        print(f'current distance: {math.dist(x,  Tlochistory[-1] )}')
        # if distance == 2 Move stright
        if(math.dist(x,  Tlochistory[-1] ) == 2):
            print(f'stright move. H:{x} T:{Tlochistory[-1]}')
            aa = np.array(x)
            bb = np.array(Tlochistory[-1])
            cc = np.subtract(aa,bb)
            print(cc)
            if (cc[0] == 2 and cc[1] == 0):
                print('move 1 to the right')
                # print(f'new: {[Tlochistory[-1][0] +1,Tlochistory[-1][1]]}')
                Tlochistory.append([Tlochistory[-1][0] +1,Tlochistory[-1][1]])
            if (cc[0] == -2 and cc[1] == 0):
                print('move 1 to the left')
                Tlochistory.append([Tlochistory[-1][0] -1,Tlochistory[-1][1]])
            if (cc[0] == 0 and cc[1] == 2):
                print('move 1 to the up')
                Tlochistory.append([Tlochistory[-1][0] ,Tlochistory[-1][1] +1] )
            if (cc[0] == 0 and cc[1] == -2):
                print('move 1 to the down')
                Tlochistory.append([Tlochistory[-1][0] ,Tlochistory[-1][1]  -1])

            # Tlochistory.append(Hlochistory[loc -1])
        # if distance > 2 diag reqiured
        elif(math.dist(x,  Tlochistory[-1] ) > 2):
            print(f'diag move. H:{x} T:{Tlochistory[-1]}')
            aa = np.array(x)
            bb = np.array(Tlochistory[-1])
            cc = np.subtract(aa,bb)
            print(cc)
            if (cc[0] > 0 and cc[1] > 0):
                print('move 1 to the up and right')
                # print(f'new: {[Tlochistory[-1][0] +1,Tlochistory[-1][1]]}')
                Tlochistory.append([Tlochistory[-1][0] +1,Tlochistory[-1][1] +1])
            if (cc[0] < 0 and cc[1] < 0):
                print('move 1 to the down and left')
                # print(f'new: {[Tlochistory[-1][0] +1,Tlochistory[-1][1]]}')
                Tlochistory.append([Tlochistory[-1][0] -1,Tlochistory[-1][1] -1])
            if (cc[0] > 0 and cc[1] < 0):
                print('move 1 to the down and right')
                # print(f'new: {[Tlochistory[-1][0] +1,Tlochistory[-1][1]]}')
                Tlochistory.append([Tlochistory[-1][0] +1,Tlochistory[-1][1] -1])
            if (cc[0] < 0 and cc[1] > 0):
                print('move 1 to the up and left')
                # print(f'new: {[Tlochistory[-1][0] +1,Tlochistory[-1][1]]}')
                Tlochistory.append([Tlochistory[-1][0] -1,Tlochistory[-1][1] +1])
        else:
            # no movment
            print('No Move')
            Tlochistory.append(Tlochistory[-1])

        print(f'loc count{loc}')
        loc += 1
    return Tlochistory






# print(generateHistory(Hlochistory))

Tlochistory = generateHistory(Hlochistory)
print('')
print(Hlochistory)
print(Tlochistory)
print('')
# count uniqe points
uniquemaker = []
for x in Tlochistory:
    if x not in uniquemaker:
        uniquemaker.append(x)

UnThistorypoints = len(uniquemaker)

print(f'The Unique Tail Points: {UnThistorypoints}')




input()

knot2 = generateHistory(Tlochistory)
knot3 = generateHistory(knot2)
knot4 = generateHistory(knot3)
knot5 = generateHistory(knot4)
knot6 = generateHistory(knot5)
knot7 = generateHistory(knot6)
knot8 = generateHistory(knot7)
knot9 = generateHistory(knot8)




input()



# So lets say that T moves R4  [[0,0],[1,0],[2,0],[3,0],[4,0]]

inb = Hlochistory

arr = np.array(inb)

# x axis values
x = arr[:,0]
# corresponding y axis values
y = arr[:,1]
  
# plotting the points 
plt.plot(x, y, color='green', linestyle='solid', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=12)


inc = Tlochistory

arr = np.array(inc)

# x axis values 
x = arr[:,0]
# corresponding y axis values
y = arr[:,1]
  
# plotting the points 
plt.plot(x, y, color='yellow', linestyle='solid', linewidth = 1,
         marker='*', markerfacecolor='red', markersize=10)


inc = knot8

arr = np.array(inc)

# x axis values 
x = arr[:,0]
# corresponding y axis values
y = arr[:,1]
  
# plotting the points 
plt.plot(x, y, color='blue', linestyle='solid', linewidth = 1,
         marker='*', markerfacecolor='red', markersize=3)
  
# setting x and y axis range
plt.ylim(-20,30)
plt.xlim(-20,30)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Head Motion Graph')
  
# function to show the plot
plt.show()