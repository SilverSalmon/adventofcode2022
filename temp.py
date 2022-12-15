
import numpy as np
import math




def reducinator(innumber):
    # The tests are divisors 23*19*13*17 and all are prime. so dividing evenly by 2,3,4,5,6 should do it?
    checks = [2,3,4,5,6,7,8,9,10,11,12]
    for x in checks:
        if innumber%x == 0:
            innumber = innumber/x
    
    return innumber



print(reducinator(97))


monkeylist0 = [79, 98]
monkeylist1 = [54, 65, 75, 74]
# monkeylist2 = [79, 60, 97]
# monkeylist3 = [74]

for x in range(0,len(monkeylist0)):
    monkeylist0[x]= reducinator(monkeylist0[x])

for x in range(0,len(monkeylist1)):
    monkeylist1[x]= reducinator(monkeylist1[x])

print(monkeylist0)
print(monkeylist1)

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

