import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

print('Day 11')



monkeylist0 = [63, 84, 80, 83, 84, 53, 88, 72]
monkeylist1 = [67, 56, 92, 88, 84]
monkeylist2 = [52]
monkeylist3 = [59, 53, 60, 92, 69, 72]
monkeylist4 = [61, 52, 55, 61]
monkeylist5 = [79, 53]
monkeylist6 = [59, 86, 67, 95, 92, 77, 91]
monkeylist7 = [58, 83, 89]

m0t = 0
m1t = 0
m2t = 0
m3t = 0
m4t = 0
m5t = 0
m6t = 0
m7t = 0


def Monkey0():
    # print('Monkey0 Turn')
    templist = monkeylist0[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] * 11
        # new = math.floor(new/3)        
        if new%13 == 0:
            monkeylist4.append(new)
        else:
            monkeylist7.append(new)
        monkeylist0.pop()
        global m0t
        m0t += 1
        
    


def Monkey1():
    # print('Monkey1 Turn')
    templist = monkeylist1[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] + 4
        # new = math.floor(new/3)
        if new%11 == 0:
            monkeylist5.append(new)
        else:
            monkeylist3.append(new)
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
        if new%2 == 0:
            monkeylist3.append(new)
        else:
            monkeylist1.append(new)
        monkeylist2.pop()
        global m2t
        m2t += 1
    

def Monkey3():
    # print('Monkey3 Turn')
    templist = monkeylist3[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] + 2
        # new = math.floor(new/3)
        if new%5 == 0:
            monkeylist5.append(new)
        else:
            monkeylist6.append(new)
        monkeylist3.pop()
        global m3t
        m3t += 1


def Monkey4():
    # print('Monkey4 Turn')
    templist = monkeylist4[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] + 3
        # new = math.floor(new/3)
        if new%7 == 0:
            monkeylist7.append(new)
        else:
            monkeylist2.append(new)
        monkeylist4.pop()
        global m4t
        m4t += 1



def Monkey5():
    # print('Monkey5 Turn')
    templist = monkeylist5[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] + 1
        # new = math.floor(new/3)
        if new%3 == 0:
            monkeylist0.append(new)
        else:
            monkeylist6.append(new)
        monkeylist5.pop()
        global m5t
        m5t += 1



def Monkey6():
    # print('Monkey6 Turn')
    templist = monkeylist6[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] + 5
        # new = math.floor(new/3)
        if new%19 == 0:
            monkeylist4.append(new)
        else:
            monkeylist0.append(new)
        monkeylist6.pop()
        global m6t
        m6t += 1



def Monkey7():
    # print('Monkey7 Turn')
    templist = monkeylist7[:]
    for x in range(len(templist)):
        # print(f'loop:{x} item:{templist[x]}')
        new = templist[x] * 19
        # new = math.floor(new/3)
        if new%17 == 0:
            monkeylist2.append(new)
        else:
            monkeylist1.append(new)
        monkeylist7.pop()
        global m7t
        m7t += 1




def reducinator(innumber):
    # The tests are divisors 23*19*13*17 and all are prime. so dividing evenly by 2,3,4,5,6 should do it?

    if(innumber> 10000):
        checks = [13*11*2*5*7*3*19*17]
        # checks = [23,19,13,17]
        for x in checks:
            # if innumber%x == 0:
            #     innumber = innumber/x
            innumber = innumber%x
        
    return innumber



 
for x in range(0,20):
    print(f'round {x+ 1}')
    Monkey0()
    Monkey1()
    Monkey2()
    Monkey3()
    Monkey4()
    Monkey5()
    Monkey6()
    Monkey7()
    
      
    # for x in range(0,len(monkeylist0)):
    #     monkeylist0[x]= reducinator(monkeylist0[x])

    # for x in range(0,len(monkeylist1)):
    #     monkeylist1[x]= reducinator(monkeylist1[x])

    # for x in range(0,len(monkeylist2)):
    #     monkeylist2[x]= reducinator(monkeylist2[x])

    # for x in range(0,len(monkeylist3)):
    #     monkeylist3[x]= reducinator(monkeylist3[x])

      
    # for x in range(0,len(monkeylist4)):
    #     monkeylist4[x]= reducinator(monkeylist4[x])

    # for x in range(0,len(monkeylist5)):
    #     monkeylist5[x]= reducinator(monkeylist5[x])

    # for x in range(0,len(monkeylist6)):
    #     monkeylist6[x]= reducinator(monkeylist6[x])

    # for x in range(0,len(monkeylist7)):
    #     monkeylist7[x]= reducinator(monkeylist7[x])

 





print(m0t)
print(m1t)
print(m2t)
print(m3t)
print(m4t)
print(m5t)
print(m6t)
print(m7t)


print(340*346) # CORRRECT

input()
