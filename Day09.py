import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# Day 9



# Read in data

df1 = pd.read_csv("input9b.txt",delimiter = ' ', engine='python' , header=None)
df1.columns =  ['direction', 'steps']
    
print(df1)

# Rules of motion


Hloc= [0,0]
Tloc= [0,0]
Hlochistory = [[0,0]]
Tlochistory = [[0,0]]

# Get Header history in an array.
for idx, row in df1.iterrows():
    print(f'move {row.direction} {row.steps} steps')
    if(row.direction == 'R'):
        print(f'Move R {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0] +1 , Hloc[1]]
            Hlochistory.append(Hloc)
    if(row.direction == 'L'):
        print(f'Move L {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0]  -1 , Hloc[1]]
            Hlochistory.append(Hloc)
    if(row.direction == 'U'):
        print(f'Move U {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0] , Hloc[1] +1]
            Hlochistory.append(Hloc)
    if(row.direction == 'D'):
        print(f'Move D {row.steps})')
        for x in range(row.steps):
            Hloc = [Hloc[0] , Hloc[1] -1]
            Hlochistory.append(Hloc)

# print(Hlochistory)

# Generate Tlochistory
loc = 0
for x in Hlochistory:
    print(f'H is at {x}. T is at {Tlochistory[-1]}')
    print(f'current distance: {math.dist(x,  Tlochistory[-1] )}')
    # if distance >2 move T to H prev location.
    if(math.dist(x,  Tlochistory[-1] ) >= 2):
        Tlochistory.append(Hlochistory[loc -1])
    loc += 1




print(Tlochistory)

uniquemaker = []
for x in Tlochistory:
    if x not in uniquemaker:
        uniquemaker.append(x)

print(uniquemaker)
    




# Count the uniqe points
UnThistorypoints = len(uniquemaker)

print(f'The Unique Tail Points: {UnThistorypoints}')


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
  
# setting x and y axis range
plt.ylim(-150,550)
plt.xlim(-200,25)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Head Motion Graph')
  
# function to show the plot
plt.show()