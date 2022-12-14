import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# Day 9



# Read in data

df1 = pd.read_csv("input9.txt",delimiter = ' ', engine='python' , header=None)
df1.columns =  ['direction', 'steps']
    
print(df1)

# Rules of motion


Hloc= [0,0]
Hlochistory = []


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

# we now have all the movements of Head

# print(Hlochistory)


def newkidloc ( kid , parent):
    # print(f'kid:{kid} parent:{parent}')
    # print(f'current distance: {math.dist(kid,  parent )}')
    dist = math.dist(kid,  parent )
    deltaX = parent[0] - kid[0]
    deltaY = parent[1] - kid[1]
    degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180
    outloc = kid
    # print(f'deltaX:{deltaX} deltaY:{deltaY} degrees:{degrees_temp}')

    if (dist > 2.9):
        print('SOMETHING IS WRONG! PARENT TOO FAR FROM KID!')
    
    if(dist == 2):
        if(degrees_temp == 90):
            outloc = [kid[0]+1, kid[1]]
        if(degrees_temp == 0):
            outloc = [kid[0], kid[1]+1]
        if(degrees_temp == -90):
            outloc = [kid[0]-1, kid[1]]
        if(degrees_temp == 180):
            outloc = [kid[0], kid[1]-1]
        
    if(dist >2):   
        if(degrees_temp > 0 and degrees_temp < 90):
            outloc = [kid[0]+1, kid[1]+1]
        if(degrees_temp > 90 and degrees_temp < 180):
            outloc = [kid[0]+1, kid[1]-1]
        if(degrees_temp > -90 and degrees_temp < 0):
            outloc = [kid[0]-1, kid[1]+1]
        if(degrees_temp > -179 and degrees_temp < -90):
            outloc = [kid[0]-1, kid[1]-1]
    # print(f'outlock:{outloc}')
    return(outloc)


def genhistory (parenthistory):
    outh = [[0,0]]
    for x in range(1,len(parenthistory)):
        outh.append(newkidloc(outh[-1],parenthistory[x]))
    return outh


k1h = genhistory(Hlochistory)
k2h = genhistory(k1h)
k3h = genhistory(k2h)
k4h = genhistory(k3h)
k5h = genhistory(k4h)
k6h = genhistory(k5h)
k7h = genhistory(k6h)
k8h = genhistory(k7h)
k9h = genhistory(k8h)


# print(Hlochistory)
# print(k1h)
# print(k2h)
# print(k3h)
# print(k4h)
# print(k5h)
# print(k6h)
# print(k7h)
# print(k8h)
# print(k9h)


# count uniqe points
uniquemaker = []
for x in k9h:
    if x not in uniquemaker:
        uniquemaker.append(x)

UnThistorypoints = len(uniquemaker)

print(f'The Unique Tail Points: {UnThistorypoints}')




input()
