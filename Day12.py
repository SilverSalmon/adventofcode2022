import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

print('Day 12 Part 1')



def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []



# # a dictionary of all points and what points they are connected too.
# graph = {}
# graph[1] = {2, 5}
# graph[2] = {1, 3, 5}
# graph[3] = {2, 4}
# graph[4] = {3, 5, 6}
# graph[5] = {1, 2, 4}
# graph[6] = {4}


# a dictionary of all points and what points they are connected too.
graph = {}
graph[1] = {2, 5}
graph[2] = {1, 3, 5}
graph[3] = {2, 4}
graph[4] = {3, 5, 6}
graph[5] = {1, 2, 4}
graph[6] = {4}

# print(graph)


# shortest_path(graph ,1,6)


# print(shortest_path(graph ,1,6))

# neato.

# Read in the file and convert to 2 D List
a = []
f = open('input12.txt')

for line in f:
    a.append(line.rstrip('\n'))

f.close()

zz = []
for l in range(0,len(a)):
    to_array = [char for char in a[l]]
    zz.append(to_array)

a = zz





startend = []

for l in range(0,len(a)):
    for c in range(0,len(a[0])):
        if a[l][c] == 'S':
            startend.append(['start',l,c])
            a[l][c] = 'a'
        if a[l][c] == 'E':
            startend.append(['end',l,c])
            a[l][c] = 'z'
            print(f'newend:{a[l][c]}')

print(startend)







# dict lookup.  key is 1 based, coord is l (line) , c (col)
lookind = 1
lookup = []
for l in range(0,len(a)):
    for c in range(0,len(a[0])):
        lookup.append([lookind,l,c,str(l) +':'+ str(c), a[l][c] ])
        lookind += 1

print('lookup:')
print(lookup)

# input()
# # # # How to get a key from a loc string:
# # hello = [entry for entry in lookup if entry[3] == '4:6'][0][0] 

# # print(hello)

# input()







# input()
# loop through the grid and log what is connected to what.
numberoflines = len(a)
numberofcols = len(a[0])


count= 0
logger = []
for l in range(0,len(a)):
    for c in range(0,len(a[0])):
        count += 1
        print(f'{a[l][c]} is at location:{l},{c} dictkey = {count}')
        temp = []
        # # look around. Up
        if l > 0:
            print( a[l -1][c] )
            if ord(a[l][c]) >= ord(a[l -1][c]) - 1 :
                print(f'connected {ord(a[l -1][c])}')
                temp.append([l-1,c])
        # Right
        if c < numberofcols -1:
            print( a[l][c +1] )
            if ord(a[l][c]) >= ord(a[l][c +1]) - 1:
                print('connected')
                temp.append([l,c+1])
        # Down
        if l < numberoflines -1:  
            print( a[l + 1][c] )
            if ord(a[l][c]) >= ord(a[l + 1][c]) - 1:
                print(f'connected Down: {a[l][c]}  {a[l + 1][c]}')
                temp.append([l+1,c])
        # Left
        if c > 0:
            print( a[l][c -1] )
            if ord(a[l][c]) >=  ord(a[l][c -1]) - 1:
                print('connected')
                temp.append([l,c-1])
        logger.append(temp)
        # input()
#  need to map the input.  and make a graph.  a given point is connected to another point if it is  lower, the same or up to 1 step higher.

print(f'The count of positions is {count}')

print(a)

print(logger)




graph2 = {}
key = 0
for aa in logger:
    key += 1
    print(f'logger to dict. key {key} for {aa}')
    listtemp = []
    for bb in aa:
        # print(''.join([str(x) for x in bb]))
        # print(   [entry for entry in lookup if entry[3] == str(':'.join([str(x) for x in bb]))][0][0]  )
        listtemp.append(str([entry for entry in lookup if entry[3] == str(':'.join([str(x) for x in bb]))][0][0]))
        # strtemp = ''
        # for cc in bb:
        #     print (cc)
    graph2[key] = {int(entry) for entry in listtemp}
    #  for ii in listtemp:
    #     graph2[key] =  

    # # How to get a key from a loc string:
    # hello = [entry for entry in lookup if entry[3] == '4:6'][0][0] 

    # input()


# graph[1] = {2, 5}
# graph[2] = {1, 3, 5}
# graph[3] = {2, 4}
# graph[4] = {3, 5, 6} 
# graph[5] = {1, 2, 4}
# graph[6] = {4}


print(graph)
print(graph2)

print(startend)
# for x in startend:
#     print(x)

print(startend[0])
print(startend[1])

print(str(startend[0][1]) +':' + str(startend[0][1]))
print(str(startend[1][1]) +':' + str(startend[1][1]))


start = [entry for entry in lookup if entry[3] == str(str(startend[0][1]) +':' + str(startend[0][2]))][0][0] 
end =  [entry for entry in lookup if entry[3] == str(str(startend[1][1]) +':' + str(startend[1][2]))][0][0] 


print(f'start:{start} end:{end}')
path = shortest_path(graph2 ,start,end)
print(path)
print(f'the answer is {len(path) -1} for part 1')


# input()





print('begin part 2')

shortesta = []

for x in lookup:
    # print(x)
    if x[4] == 'a':
        # print(x[0])
        shortesta.append([shortest_path(graph2 ,x[0],end) ,x[0], end   ])



# shortesta.sort()
# print(shortesta)
pathlen = []
for x in shortesta:
    print(f'steps: {len(x[0]) -1} path:{x[0]} s:{x[1]} e:{x[2]}')
    if len(x[0]) > 0:
        pathlen.append(len(x[0])-1)

pathlen.sort()



print(f'The shortest path is { pathlen[0]}')

input()
