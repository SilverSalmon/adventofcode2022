import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

print('Day 11')



monkeylist0 = [79, 98]
monkeylist1 = [54, 65, 75, 74]
monkeylist2 = [79, 60, 97]
monkeylist3 = [74]

m0t = 0
m1t = 0
m2t = 0
m3t = 0


def Monkey0():
    # print('Monkey0 Turn')
    templist = monkeylist0[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] * 19
        # new = math.floor(new/3)        
        if new%23 == 0:
            monkeylist2.append(new)
        else:
            monkeylist3.append(new)
        monkeylist0.pop()
        global m0t
        m0t += 1
        
    


def Monkey1():
    # print('Monkey1 Turn')
    templist = monkeylist1[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] + 6
        # new = math.floor(new/3)
        if new%19 == 0:
            monkeylist2.append(new)
        else:
            monkeylist0.append(new)
        monkeylist1.pop()
        global m1t
        m1t += 1
    

def Monkey2():
    # print('Monkey2 Turn')
    templist = monkeylist2[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] * templist[x]
        # new = math.floor(new/3)
        if new%13 == 0:
            monkeylist1.append(new)
        else:
            monkeylist3.append(new)
        monkeylist2.pop()
        global m2t
        m2t += 1
    

def Monkey3():
    # print('Monkey3 Turn')
    templist = monkeylist3[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] + 3
        # new = math.floor(new/3)
        if new%17 == 0:
            monkeylist0.append(new)
        else:
            monkeylist1.append(new)
        monkeylist3.pop()
        global m3t
        m3t += 1


 

def finddivisors(val):
    out = []
    for x in range(1,val+1):
        if(val%x==0):
            out.append(x)
    return(out)

def reducinator(innumber):
    # The tests are divisors 23*19*13*17 and all are prime. so dividing evenly by 2,3,4,5,6 should do it?

    if(innumber> 10000):
        checks = [23*19*13*17]
        # checks = [23,19,13,17]
        for x in checks:
            # if innumber%x == 0:
            #     innumber = innumber/x
            innumber = innumber%x
        
    return innumber




for x in range(0,10000):
    print(f'round {x+ 1}')
    Monkey0()
    Monkey1()
    Monkey2()
    Monkey3()

        
    for x in range(0,len(monkeylist0)):
        monkeylist0[x]= reducinator(monkeylist0[x])

    for x in range(0,len(monkeylist1)):
        monkeylist1[x]= reducinator(monkeylist1[x])

    for x in range(0,len(monkeylist2)):
        monkeylist2[x]= reducinator(monkeylist2[x])

    for x in range(0,len(monkeylist3)):
        monkeylist3[x]= reducinator(monkeylist3[x])


    # print(f'round {x +1} end')
    # print(monkeylist0)
    # print(monkeylist1)
    # print(monkeylist2)
    # print(monkeylist3)
    # input()





print(m0t)
print(m1t)
print(m2t)
print(m3t)


results = [m0t,m1t,m2t,m3t]

results.sort()

results.reverse()

print(results[0] * results[1])



input()




# for x in monkeylist0:
#     if x % (23*19*13*17) == 0:
#         print(x)



# print(23*19*13*17)