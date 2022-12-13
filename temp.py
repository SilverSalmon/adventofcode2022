
import numpy as np

a = []

f = open('input8b.txt')

for line in f:
    a.append(line.rstrip('\n'))

f.close()

print(a)





def split_str(s):
    return [c for c in s]


grid = []

# Print
for x in a: 
    print(x)
    aa = str(x)
    t = split_str(aa)
    grid.append(t)

print(grid)


for  x in range(0,len(grid)):
    print(''.join(grid[x]))

print(f'height = {len(grid)}')
print(f'length = {len(str(a[0][0]))}')
 

xx = input()