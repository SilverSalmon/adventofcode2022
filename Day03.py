import pandas as pd
import numpy as np




pdinput = pd.read_csv("input3.txt",sep = ' ', header=None, names=["init"])




pdinput['thelength'] =   (pdinput['init'].apply(len) /2).astype(int)

pdinput['first'] =   pdinput.apply(lambda x: x['init'][:x['thelength']], axis=1)   

pdinput['second'] = pdinput.apply(lambda x: x['init'][x['thelength']:], axis=1)   

# find the intersections as a set
pdinput["common_letters_set"] = pdinput.apply(
    lambda x: set(x["first"]).intersection(set(x["second"])),
    axis=1)

# turn the set into just a letter
pdinput['common_letter'] = pdinput['common_letters_set'].str.join(', ')



print('testing priority')

def value(letter):
    out = 0
    if letter.isupper() == True:
        out = ord(letter) - ord('a') + 59
        # print ('upper')
    else:
        out = ord(letter) - ord('a') + 1
        # print ('lower')
    # return ord(letter) - ord('a') + 1

    return out


# print(f"a = {value('a')}")


# print(f"A = {value('A')}")


# print(f"Z = {value('Z')}")



pdinput['priority'] = pdinput['common_letter'].apply(value)



# print(pdinput)


print(f"The answer for part one is:{pdinput['priority'].sum()}")




# part 2
pdinput = pd.read_csv("input3.txt",sep = ' ', header=None, names=["init"])


print(pdinput.head(4))

# Break into different columns
df1 = pdinput[pdinput.index % 3 == 0]
df2 = pdinput[pdinput.index % 3 == 1]
df3 = pdinput[pdinput.index % 3 == 2]

# create new index for joining
df1.reset_index(inplace = True)
df2.reset_index(inplace = True)
df3.reset_index(inplace = True)

print(df1)

df1 = df1.join(df2['init'] ,lsuffix='first', rsuffix='second')
df1 = df1.join(df3['init'] , rsuffix='third')
# rename cols
df1.columns = ['initindex','first', 'second','third']



# find the intersections as a set
df1["common_letters_set"] = df1.apply(
    lambda x: set(x["first"]).intersection(set(x["second"]).intersection(set(x["third"])   )),
    axis=1)

# turn the set into just a letter
df1['common_letter'] = df1['common_letters_set'].str.join(', ')


df1['priority'] = df1['common_letter'].apply(value)



# print(pdinput)


print(f"The answer for part two is:{df1['priority'].sum()}")

# print (df1)