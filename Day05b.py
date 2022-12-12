import pandas as pd
import numpy as np



df1 = pd.read_csv("input5.txt",delimiter = ' ', engine='python' , header=None)


dfx = pd.read_csv("input5.txt", engine='python' , header=None)

# Only get inputs.
df2 = dfx.head(8)

s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []

for idx, row in df2.iterrows():
    # print(row[0][5:6])

    print(row[0][9:10])
    s1.append(row[0][1:2])
    s2.append(row[0][5:6])
    s3.append(row[0][9:10])
    s4.append(row[0][13:14])
    s5.append(row[0][17:18])
    s6.append(row[0][21:22])
    s7.append(row[0][25:26])
    s8.append(row[0][29:30])
    s9.append(row[0][33:34])

#  remove spaces
while ' ' in s3:
    s3.remove(' ')

while ' ' in s5:
    s5.remove(' ')
    
while ' ' in s6:
    s6.remove(' ')


while ' ' in s7:
    s7.remove(' ')


while ' ' in s8:
    s8.remove(' ')


while ' ' in s9:
    s9.remove(' ')


# Check
print("INPUT CHECK:")
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)






def mover(amount,  arrfrom,  arrto):

    arrfromx = globals()[arrfrom]
    arrtox = globals()[arrto]
    # global s8
    # global s4
    # print(amount)
    # print(arrfrom)
    # print(arrto)
    z = []
    for x in range(0,int(amount)):
        x = arrfromx.pop(0)
        z.insert(0, x)
    # z.reverse()

    for xx in z:
        arrtox.insert(0, xx)

 


# slice off the top 9 rows
df1 = df1[9:]


df1 = df1.iloc[:,0:6]

df1.columns = ['wmove','amoutn','wfrom','from','wto','to']

df1['from'] = 's' + df1['from'].astype(str)
df1['to'] = 's' + df1['to'].astype(str)

print(df1)





print('before')
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)




for idx, row in df1.iterrows():
    
    print(idx, row['amoutn'], row['from'], row['to'])
    mover(row['amoutn'], row['from'], row['to'])

    



print('after')
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)

print( s1[0] +s2[0]  +s3[0] +s4[0] +s5[0] +s6[0] +s7[0] +s8[0] +s9[0] )