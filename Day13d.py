import ast


print('Day 13 Attempt C PART 2')

# Open file and load as array a:
a = []
f = open('input13.txt')
for line in f:
    a.append(line.rstrip('\n'))
f.close()

# Load the pairs to compare to leftarray and rightarray:
leftarray = []
rightarray = []
part2array = []
for x in range(0,len(a)):
    if (x +3)%3 == 0:
        leftarray.append(ast.literal_eval(a[x]))
        part2array.append(ast.literal_eval(a[x]))
    if (x+2)%3 == 0:
        rightarray.append(ast.literal_eval(a[x]))
        part2array.append(ast.literal_eval(a[x]))

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
    # print(f'Compare l:{l} length({len(l)}) type({type(l)})  vs r:{r}  length({len(r)}) type({type(r)})')

    flag = 'notset'
    rangeval = shortestlistlen(l,r)[0]
    tietest = shortestlistlen(l,r)[1]
    for x in range(0,rangeval):
        # print(shortestlistlen(l,r)[1])
        
        # print(l[x])
        # print(r[x])
        if type(l[x]) == list and type(r[x]) == list:
            # print('call self')
            p = comparit(l[x],r[x], ix)
        
        if type(l[x]) == int and type(r[x]) == list:
            # print('lisint')
            p = comparit([l[x]],r[x],ix)
            if p != 'notset':
                break
        
        if type(l[x]) == list and type(r[x]) == int:
            # print('risint')
            p = comparit(l[x],[r[x]],ix)
            if p != 'notset':
                break
        
        if type(l[x]) == int and type(r[x]) == int:
            # print('both int')
            if l[x] < r[x]:
                flag = 'good'
                record.append(['good',ix])
                break
            if l[x] > r[x]:
                flag = 'bad'
                record.append(['bad',ix])
                break
    if(len(record)== 0 or isnoentry(ix)):
        # print('tiebreaker?')
        if (tietest) == 'b is longer':
                flag = 'good'
                record.append([flag,ix])
        if (tietest) == 'a is longer':
                flag = 'bad'
                record.append([flag,ix])
    return flag


for x in range(0,len(rightarray)):
    comparit(leftarray[x], rightarray[x], x)
    # print(record)
    # input()

# comparit(leftarray[1], rightarray[1], 1)

# print(record)

# remove stupid dups frou double tie breaks.a
recordfixed = []
prevflag = -1
for xx in range(0,len(record)):
    if xx > 0:
        prevflag = record[xx -1][1]
    if record[xx][1] != prevflag:
        recordfixed.append(record[xx])

# print(recordfixed)

record = recordfixed



bb = []
countz = 1
for zzq in record:
    if zzq[0]== 'good':
        bb.append(countz)
    countz += 1

# print(bb)

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 0
    for x in myList:
        result = result + x
    return result



print(multiplyList(bb))  
#  6086 is the correct answer

print('Welcome to Part 2')



record = []
for x in record:
    record.pop()

iscorcount = 0





def iscorrect(l,r):
    global iscorcount
    # print(f'record before: {record}')
    comparit(l, r, iscorcount)
    # print(f'record after: {record}')
    if record[0][0] == 'good':
        print(f'comparing l {l} to {r} and l found to be smaller')
        while record:
            record.pop()
        return True
    else:
        print(f'comparing l {l} to {r} and l found to be bigger')
        while record:
            record.pop()
        return False
    
    






def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # if arr[j] > arr[j + 1]:
            if iscorrect(arr[j],arr[j+1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
 
 



part2array.append([[2]])
part2array.append([[6]])

# Driver code to test above
# arr = [[[2]],[4],[3],[[4,4],4,4],[[4,4],4,4,4]]
# arr = [[1],[3],[2]]
arr = [[1,1,5,1,1], [[1],4],[[2]] ]
print(arr)
print(part2array)


bubbleSort(arr)
bubbleSort(part2array)

arr.reverse()
part2array.reverse()

print('bubbleTest1')
print(arr) 
print(part2array)

print('')
input()

# part2array.reverse()
# print(part2array)

print('print after bubble sort')
for x in part2array:
    print(x)

input('nopresort')


low = 0
high = 0
for x in range(0,len(part2array)):
    if part2array[x] == [[2]]:
        low = x+1
    if part2array[x] == [[6]]:
        high = x+1

answer = low * high
print(f'The answer to part two is {answer}')
#  32558 is wrong

input()