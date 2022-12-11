# Day 1
import pandas as  pd

print("Hello Day 1")


#  need to read in a big input

biggestsum = 0
currentsum = 0
arrayofsums = []

with open('input.txt') as f:
    for line in f:
        if line in ['\n', '\r\n']:
            if currentsum > biggestsum:
                biggestsum = currentsum
            arrayofsums.append(currentsum)
            currentsum = 0
        else:
            currentsum = currentsum + int(line)
        #
# Part 1 
print(biggestsum)

#create new df 
df = pd.DataFrame({'col1':arrayofsums})

print (df.sort_values(by=['col1'], ascending=False).head(3))

# Part 2
print (df.sort_values(by=['col1'], ascending=False).head(3).sum())