import pandas as pd
import numpy as np


# Read input
df1 = pd.read_csv("input7.txt",delimiter = ' ', engine='python' , header=None)

# Create Group IDs based on where 0s are
groups = df1[1].eq('cd').cumsum()

# Groupby groups and transform each group to the size
df1['Count'] = df1.groupby(groups)[1].transform('size')

currentloc =[]
tempsum = 0
outputloc = []
outputsum = []


# loop through and get long filenames
for idx, row in df1.iterrows():
    # print(row[0], row[1], row[2], row['Count'])

    if(row[0] =='$' and row[1] =='cd' and row[2] !='..'):
        currentloc.append(row[2])
        # print(f'command $cd {row[2]}')
        # print(currentloc)
        xx = ' '.join(currentloc)
        # print(f'sum of files = {tempsum}')
        # df = df.append({'dir': currentloc, 'subtotal' : tempsum}, ignore_index=True)
        
        outputsum.append(tempsum)
        tempsum = 0
    if(row[0] =='$' and row[1] =='cd' and row[2] =='..'):
        currentloc.pop()
        # print(f'command $cd {row[2]}')
        # print(currentloc)
    # if(row[0] =='$' and row[1] =='ls'):
    #     pass
    #     # print('listing')
    # if(row[0] =='dir'):
    #     pass
    #     print('subdirictory found')
    # if(row[0].isdigit()):
    #     print(row[0])
    #     tempsum = tempsum + int(row[0])
    outputloc.append(xx)


dfxx = pd.DataFrame({'longname':outputloc})


dfzz = df1.join(dfxx,lsuffix='first', rsuffix='second')

# print(dfzz)


dfzz.columns = ['c1','c2','c3','count','longname']

bigt = []
sortme = []

# Recursive Function
def howbig(indir):
    w = []
    rslt_df = dfzz.loc[dfzz['longname'] == indir] 
    w = rslt_df.values.tolist()
    sumsum = 0
    # print(w)
    for x in w:
        # if x[0] == '$':
        #     print('$')
        if x[0].isdigit():
            sumsum = sumsum + int(x[0])
        if x[0] == 'dir':
            # print(  x[4] + ' ' + x[1])
            sumsum = sumsum + howbig(x[4] + ' ' + x[1])
            # sumsum = howbig
    # the size of the directory.  If deleted would add to the free space of 19177471
    print(indir + ' ' + str(sumsum) + ' ' + str(30000000 - sumsum + 19177471))
    if sumsum < 100000:
        bigt.append(sumsum)
    sortme.append(sumsum)
    return sumsum

totused = howbig('/')

# print(bigt)
print(sum(bigt))


curfree = 70000000 - totused
print( f'total  space = 70000000')
print( f'needed space = 30000000 ')
print( f'current free space: {curfree}'   )
print( f'must delete at least: {30000000 - curfree}')
# print(30000000 - (70000000 - int (howbig('/'))))

sortme.sort()
# print(sortme)

# Find the smallest to delete:
for x in sortme:
    if x <= 10822529:
        pass
    else:
        print(x)
        break