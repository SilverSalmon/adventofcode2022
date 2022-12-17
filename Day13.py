import numpy as np
import ast


print('Day 13')


a = []
f = open('input13b.txt')

for line in f:
    a.append(line.rstrip('\n'))

f.close()

zz = []
for l in range(0,len(a)):
    # to_array = [char for char in a[l]]
    zz.append(a[l])

a = zz





print(len(a))




def getnextval(input):
    print('input')




def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])




record = []
countcompares = 0
def comparelvr(l,r):
    print(f'Compare l:{l} length({len(l)}) type({type(l)})  vs r:{r}  length({len(r)}) type({type(r)})')

    # get shorter of two lists
    counterz = 0
    if(len(l) >= len(r)):
        counterz = len(r)
    else:
        counterz = len(l)
    flag = 'same'
    for zz in range(0,counterz):
        print(f'Lets compare l: {l[zz]} to r: {r[zz]})')
        if type(l[0]) == int and type(r[0]) == int:
            if(l[zz] == r[zz]):
                flag='same'
                print('same')
            elif(l[zz] < r[zz]):
                flag='good'
            else:
                flag='bad'
            
            if flag!='same':
                global record
                record.append(flag)
                break
        
        if type(l[0]) == list and type(r[0]) == list:
            counterz2 = 0
            if(len(l) >= len(r)):
                counterz2 = len(r)
            else:
                counterz2 = len(l)
            flag = 'same'
            for zz in range(0,counterz):
                print(f'Lets compare l: {l[zz]} to r: {r[zz]})')
                if type(l[0]) == int and type(r[0]) == int:
                    if(l[zz] == r[zz]):
                        flag='same'
                        print('same')
                    elif(l[zz] < r[zz]):
                        flag='good'
                    else:
                        flag='bad'
                    
                    if flag!='same':
                        # global record
                        record.append(flag)
                        break
        if type(l[0]) == list and type(r[0]) == int:
            print('mixed')
            if l[0][0] == r[0]:
                print('mixed same')
            if l[0][0] < r[0]:
                print('good')
            else:
                print('bad')
        
        if type(l[0]) == int and type(r[0]) == list:
            print('mixed')
            if l[0] == r[0][0]:
                print('mixed same')
            if l[0] < r[0][0]:
                print('good')
            else:
                print('bad')





    # if (len(l) > 0 and len(r) > 0):
    #     print(f'pos 0 l:{l[0]} of type{type(l[0])}')
    #     print(f'pos 0 l:{r[0]} of type{type(r[0])}')

    #     # if both are ints:
    #     if type(l[0]) == int and type(r[0]) == int:
    #         print(f'both ints: {l[0]} and {r[0]}')

    #     elif type(l[0]) == list and type(r[0]) == list:
    #         print(f'both lists: {l[0]} and {r[0]}') 

    #     else:
    #         print('mixed')
        
    global countcompares
    countcompares += 1
    input()








# Iterate over the file and call the compare function.

count = 0
for x in a:
    # print(f'current count:{count} len = {len(a)}')
    if x == '':
        comparelvr(a[count-2],a[count-1])
    # Last compare not followed by an empty line.
    if count == len(a) -1:
        # print(f'last record:{a[count]}')
        comparelvr(a[count-1],a[count])
    count +=1



print(f'number of comparisons:{countcompares}')

input()