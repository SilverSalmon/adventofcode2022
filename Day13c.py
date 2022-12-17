import ast


print('Day 13 Attempt C')

# Open file and load as array a:
a = []
f = open('input13.txt')
for line in f:
    a.append(line.rstrip('\n'))
f.close()

# Load the pairs to compare to leftarray and rightarray:
leftarray = []
rightarray = []
for x in range(0,len(a)):
    if (x +3)%3 == 0:
        leftarray.append(ast.literal_eval(a[x]))
    if (x+2)%3 == 0:
        rightarray.append(ast.literal_eval(a[x]))

# a recursive function that takes in two arrays


def shortestlistlen(a,b):
    if(len(a) > len(b)):
        return [len(b),'a is longer']
    if(len(a) == len(b)):
        return [len(a),'same length']
    else:
        return [len(a),'b is longer']


record = []


def isnoentry(ix):
    for x in record:
        if x[1] == ix:
            return False
        else:
            return True

# both must be lists. if both item 0 are lists call self.  if either is int begin comparasion
def comparit(l,r,ix):
    print(f'Compare l:{l} length({len(l)}) type({type(l)})  vs r:{r}  length({len(r)}) type({type(r)})')

    flag = 'notset'
    rangeval = shortestlistlen(l,r)[0]
    tietest = shortestlistlen(l,r)[1]
    for x in range(0,rangeval):
        print(shortestlistlen(l,r)[1])
        
        print(l[x])
        print(r[x])
        if type(l[x]) == list and type(r[x]) == list:
            print('call self')
            p = comparit(l[x],r[x], ix)
        
        if type(l[x]) == int and type(r[x]) == list:
            print('lisint')
            p = comparit([l[x]],r[x],ix)
            break
        
        if type(l[x]) == list and type(r[x]) == int:
            print('risint')
            p = comparit(l[x],[r[x]],ix)
            break
        
        if type(l[x]) == int and type(r[x]) == int:
            print('both int')
            if l[x] < r[x]:
                flag = 'good'
                record.append(['good',ix])
                break
            if l[x] > r[x]:
                flag = 'bad'
                record.append(['bad',ix])
                break
    if(len(record)== 0 or isnoentry(ix)):
        print('tiebreaker?')
        if (tietest) == 'b is longer':
                flag = 'good'
                record.append([flag,ix])
        if (tietest) == 'a is longer':
                flag = 'bad'
                record.append([flag,ix])
    return flag


for x in range(0,len(rightarray)):
    comparit(leftarray[x], rightarray[x], x)
    print(record)
    # input()

# comparit(leftarray[1], rightarray[1], 1)

print(record)

# remove stupid dups frou double tie breaks.a
recordfixed = []
prevflag = -1
for xx in range(0,len(record)):
    if xx > 0:
        prevflag = record[xx -1][1]
    if record[xx][1] != prevflag:
        recordfixed.append(record[xx])

print(recordfixed)

record = recordfixed



bb = []
countz = 1
for zzq in record:
    if zzq[0]== 'good':
        bb.append(countz)
    countz += 1

print(bb)

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 0
    for x in myList:
        result = result + x
    return result



print(multiplyList(bb))























# def shortestlistlen(a,b):
#     if(len(a) > len(b)):
#         return [len(b),'a is longer']
#     if(len(a) == len(b)):
#         return [len(a),'same length']
#     else:
#         return [len(a),'b is longer']


# record = []


# def isnoentry(ix):
#     for x in record:
#         if x[1] == ix:
#             return True
#         else:
#             return False

# # both must be lists. if both item 0 are lists call self.  if either is int begin comparasion
# def comparit(l,r,ix):
#     print(f'Compare l:{l} length({len(l)}) type({type(l)})  vs r:{r}  length({len(r)}) type({type(r)})')

#     flag = 'notset'
#     rangeval = shortestlistlen(l,r)[0]
#     tietest = shortestlistlen(l,r)[1]
#     for x in range(0,rangeval):
#         print(shortestlistlen(l,r)[1])
        
#         print(l[x])
#         print(r[x])
#         if type(l[x]) == list and type(r[x]) == list:
#             print('call self')
#             p = comparit(l[x],r[x], ix)
        
#         if type(l[x]) == int and type(r[x]) == list:
#             print('lisint')
#             p = comparit([l[x]],r[x],ix)
#             break
        
#         if type(l[x]) == list and type(r[x]) == int:
#             print('risint')
#             p = comparit(l[x],[r[x]],ix)
#             break
        
#         if type(l[x]) == int and type(r[x]) == int:
#             print('both int')
#             if l[x] < r[x]:
#                 flag = 'good'
#                 record.append(['good',ix])
#                 break
#             if l[x] > r[x]:
#                 flag = 'bad'
#                 record.append(['bad',ix])
#                 break
#     if(len(record)== 0 or isnoentry(ix)):
#         if (tietest) == 'b is longer':
#                 flag = 'good'
#                 record.append([flag,ix])
#         if (tietest) == 'a is longer':
#                 flag = 'bad'
#                 record.append([flag,ix])
#     return flag



# # Iterate over the file and call the compare function.

# count = 0
# for x in a:
#     if x == '':
#         print(f'l:{a[count-2]}  r:{a[count-1]}')
#         comparit(ast.literal_eval(a[count-2]),ast.literal_eval(a[count-1]),count)
#     # Last compare not followed by an empty line.
#     if count == len(a) -1:
#         print(f'last record:{a[count]}')
#         comparit(a[count-1],a[count],count)
#     count +=1


# # print(f'number of comparisons:{countcompares}')

# print(record)


# bb = []
# countz = 1
# for zzq in record:
#     if zzq[0]== 'good':
#         bb.append(countz)
#     countz += 1

# print(bb)

# def multiplyList(myList):
 
#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#         result = result * x
#     return result



# print(multiplyList(bb))


input()