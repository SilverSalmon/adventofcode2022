import pandas as pd
import numpy as np



# aggreate all directories?

# A dir size is the sum of all the dirs and filees within.

# for each directory look for entry into directory and loop count times..
 
 

df1 = pd.read_csv("input7.txt",delimiter = ' ', engine='python' , header=None)


# Create Group IDs based on where 0s are
groups = df1[1].eq('cd').cumsum()

# Groupby groups and transform each group to the size
df1['Count'] = df1.groupby(groups)[1].transform('size')

# print(df1)



# print(tillnextcd(0))

for idx, row in df1.head(60).iterrows():
    print(row[0], row[1], row[2])




def tot


    # if(row[0] =='$' and row[1] =='cd' and row[2] !='..'):
    #     currentloc.append(row[2])
    #     print(f'command $cd {row[2]}')
    #     print(currentloc)
    #     xx = '/'.join(currentloc)
    #     print(f'sum of files = {tempsum}')
    #     # df = df.append({'dir': currentloc, 'subtotal' : tempsum}, ignore_index=True)
    #     outputloc.append(xx)
    #     outputsum.append(tempsum)
    #     tempsum = 0
    # if(row[0] =='$' and row[1] =='cd' and row[2] =='..'):
    #     currentloc.pop()
    #     print(f'command $cd {row[2]}')
    #     print(currentloc)
    # if(row[0] =='$' and row[1] =='ls'):
    #     print('listing')
    # if(row[0] =='dir'):
    #     print('subdirictory found')
    # if(row[0].isdigit()):
    #     print(row[0])
    #     tempsum = tempsum + int(row[0])


# def howbigdir(dirname):
#     for idx, row in df1.head(14).iterrows():
#         print('hi')
#         if row[2] == dirname:

# print (outputsum)
# print(outputloc)
