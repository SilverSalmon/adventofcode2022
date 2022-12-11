import pandas as pd
import numpy as np




pdinput = pd.read_csv("input2.txt",sep = ' ', header=None, names=["op","me"])




# points for playing a card?
conditions = [
    (pdinput['me'] == 'X'),
    (pdinput['me'] == 'Y'),
    (pdinput['me'] == 'Z')
    ]

values = [1,2,3]

pdinput['mepts'] = np.select(conditions, values)

# A Rock
# B Paper
# C Scisors

# X Rock
# Y Paper
# Z Scissors



conditions2 = [
    (pdinput['op'] == 'A' ) & (pdinput['me'] == 'X' ),  # Rock to Rock Tie 3
    (pdinput['op'] == 'A' ) & (pdinput['me'] == 'Y' ),  # Rock to Papper Win 6
    (pdinput['op'] == 'A' ) & (pdinput['me'] == 'Z' ),  # Rock to Sciss  lose 0
    (pdinput['op'] == 'B' ) & (pdinput['me'] == 'X' ),  # Paper to Rock Loss 0
    (pdinput['op'] == 'B' ) & (pdinput['me'] == 'Y' ),  # Paper to Paper Tie 3
    (pdinput['op'] == 'B' ) & (pdinput['me'] == 'Z' ),  # Paper to Sciss Win 6
    (pdinput['op'] == 'C' ) & (pdinput['me'] == 'X' ),  # Sis to Rock Win 6
    (pdinput['op'] == 'C' ) & (pdinput['me'] == 'Y' ),  # Scis to Paper Loss 0
    (pdinput['op'] == 'C' ) & (pdinput['me'] == 'Z' )   # Scis to scis Tie 3
    ]


values2 = [3,6,0,0,3,6,6,0,3]



pdinput['winpts'] = np.select(conditions2, values2)


pdinput['totforround'] = pdinput['mepts'] + pdinput['winpts']



print(pdinput['totforround'].sum())


# part two


# A Rock  1
# B Paper   2
# C Scisors   3


#  x = need to lose 0
#  y = need to draw 3
#  z = need to win  6


conditions3 = [
    (pdinput['me'] == 'X'),
    (pdinput['me'] == 'Y'),
    (pdinput['me'] == 'Z')
    ] 

values3 = ['lose','draw','win']

pdinput['part2'] = np.select(conditions3, values3)

# pdinput['totforround2'] = pdinput['mepts'] + pdinput['part2']


# print(pdinput['totforround2'].sum())

conditions4 = [
    (pdinput['part2'] == 'draw') & (pdinput['op'] == 'A' ), # need a draw and op has played Rock. I must play Rock which is worth 1
    (pdinput['part2'] == 'draw') & (pdinput['op'] == 'B' ), # need a draw and op has played paper. I must play paper which is worth 2
    (pdinput['part2'] == 'draw') & (pdinput['op'] == 'C' ), # need a draw and op has played scis. I must play scis which is worth  3
    (pdinput['part2'] == 'win') & (pdinput['op'] == 'A' ), # need a win and op has played Rock. I must play paper which is worth 2
    (pdinput['part2'] == 'win') & (pdinput['op'] == 'B' ), # need a win and op has played paper. I must paper scis which is worth 3
    (pdinput['part2'] == 'win') & (pdinput['op'] == 'C' ), # need a win and op has played scis. I must paper Rock which is worth  1
    (pdinput['part2'] == 'lose') & (pdinput['op'] == 'A' ), # need a lose and op has played Rock. I must paper scis which is worth 3
    (pdinput['part2'] == 'lose') & (pdinput['op'] == 'B' ), # need a lose and op has played paper. I must paper Rock which is worth  1
    (pdinput['part2'] == 'lose') & (pdinput['op'] == 'C' ) # need a lose and op has played scis. I must play paper which is worth 2
    ]


values4 = [1,2,3,2,3,1,3,1,2]


pdinput['part2b'] = np.select(conditions4, values4)

conditions5 = [
    (pdinput['me'] == 'X'),
    (pdinput['me'] == 'Y'),
    (pdinput['me'] == 'Z')
    ] 

values5 = [0,3,6]

pdinput['part2c'] = np.select(conditions5, values5)

pdinput['totforround2'] = pdinput['part2b'] + pdinput['part2c']


print(pdinput)


print(pdinput['totforround2'].sum())