
import numpy as np
import math
import ast


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
            print(f'p after self call:{p}')
            if p != 'notset':
                break
        
        if type(l[x]) == list and type(r[x]) == int:
            print('risint')
            p = comparit(l[x],[r[x]],ix)
            if p != 'notset':
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
        if (tietest) == 'b is longer':
                flag = 'good'
                record.append([flag,ix])
        if (tietest) == 'a is longer':
                flag = 'bad'
                record.append([flag,ix])
    return flag

for x in record:
    record.pop()

def iscorrect(l,r):
    comparit(l, r, 0)
    if record[0][0] == 'good':
        return True
        for x in record:
            record.pop()
    else:
        return False
        for x in record:
            record.pop()

a = [1,1,3,1,1]

b = [[1],4]

print(iscorrect(a,b))

print(record)
input()




# def getintofposition(inlist,position):
#     print(f'inlist {inlist}   position {position}   type:{type(inlist[position])}')
#     if type(inlist[position]) == int:
#         print(f'int{inlist[position]}')
#         return inlist[position]
#     else:
#         p = getintofposition(inlist[position],0)
#         return p    
   

# a = [1,2,[7,8],4,6]


# print(getintofposition(a, 3))

# print(ord('z'))
# print(ord('E'))
# input()










# def find_path(obj, val, path=''):
#     if isinstance(obj, dict):
#         for k, v in obj.items():
#             if k == val:
#                 return f'{path}[{k!r}]'
#             return find_path(v, val, path + f'[{k!r}]')
#     elif isinstance(obj, list):
#         for i, v in enumerate(obj):
#             if v == val:
#                 return f'{path}[{i!r}]'
#             return find_path(v, val, path + f'[{i!r}]') 






# def find_path(obj, val, path=''):
#     p = []
#     if isinstance(obj, dict):
#         for k, v in obj.items():
#             if k == val:
#                 return f'{path}[{k!r}]'
#             p = find_path(v, val, path + f'[{k!r}]')
#         return p
#     elif isinstance(obj, list):
#         for i, v in enumerate(obj):
#             if v == val:
#                 return f'{path}[{i!r}]'
#             p = find_path(v, val, path + f'[{i!r}]')
#         return p

# bla = find_path(ex, 'approvers')
# print(bla) # ['Resources'][0]['uschemas']['approvers']













# def reducinator(innumber):
#     # The tests are divisors 23*19*13*17 and all are prime. so dividing evenly by 2,3,4,5,6 should do it?
#     checks = [2,3,4,5,6,7,8,9,10,11,12]
#     for x in checks:
#         if innumber%x == 0:
#             innumber = innumber/x
    
#     return innumber



# print(reducinator(97))


# monkeylist0 = [79, 98]
# monkeylist1 = [54, 65, 75, 74]
# # monkeylist2 = [79, 60, 97]
# # monkeylist3 = [74]

# for x in range(0,len(monkeylist0)):
#     monkeylist0[x]= reducinator(monkeylist0[x])

# for x in range(0,len(monkeylist1)):
#     monkeylist1[x]= reducinator(monkeylist1[x])

# print(monkeylist0)
# print(monkeylist1)

# def finddivisors(val):
#     out = []
#     for x in range(1,val+1):
#         if(val%x==0):
#             out.append(x)
#     return(out)

# print(finddivisors(26944422764546))

# input()

# print(math.floor(500/3))

# # x = range(16)

# x = np.reshape(x,(4,4))
# print(x)

# print(' ')

# print(x[:,0])









# inb = [[0,0],[1,0],[2,0],[3,0],[4,0]]

# arr = np.array(inb)

# print(arr)

# print(' ')

# brr = arr[1:1,0]

# print(brr)

