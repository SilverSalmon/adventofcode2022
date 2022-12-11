import pandas as pd
import numpy as np



df1 = pd.read_csv("input4.txt",delimiter = ',', engine='python' , header=None, names=["col1","col2"])



df2 = df1['col1'].str.split('-', expand = True)
df3 = df1['col2'].str.split('-', expand = True)

df = df2.join(df3,lsuffix='first', rsuffix='second')
df.columns = ['Alow','Ahigh','Blow','Bhigh']
df['Alow'] = df['Alow'].astype(int)
df['Ahigh'] = df['Ahigh'].astype(int)
df['Blow'] = df['Blow'].astype(int)
df['Bhigh'] = df['Bhigh'].astype(int)

# print(df.to_string(index=False))

conditions2 = [
    # (pdinput['op'] == 'A' ) & (pdinput['me'] == 'X' ),  
    (df['Alow'] >= df['Blow']) & (df['Ahigh'] <= df['Bhigh']),
    (df['Alow'] <= df['Blow']) & (df['Ahigh'] >= df['Bhigh']),
    (df['Alow'] <= df['Blow']) & (df['Ahigh'] <= df['Bhigh']),
    (df['Alow'] >= df['Blow']) & (df['Ahigh'] >= df['Bhigh'])
    ]

#    8    37   37    91

values2 = [1,1,0,0]



df['containscheck'] = np.select(conditions2, values2)


pd.set_option('display.max_rows', None)

#view DataFrame
# print(df.to_string(index=False))

print(f"The answer for part one is:{df['containscheck'].sum()}")





# part 2



df1 = pd.read_csv("input4.txt",delimiter = ',', engine='python' , header=None, names=["col1","col2"])



df2 = df1['col1'].str.split('-', expand = True)
df3 = df1['col2'].str.split('-', expand = True)

df = df2.join(df3,lsuffix='first', rsuffix='second')
df.columns = ['Alow','Ahigh','Blow','Bhigh']
df['Alow'] = df['Alow'].astype(int)
df['Ahigh'] = df['Ahigh'].astype(int)
df['Blow'] = df['Blow'].astype(int)
df['Bhigh'] = df['Bhigh'].astype(int)

# print(df.to_string(index=False))


# how to have any overlap?  if the Alow is less than blow
conditions2 = [
    # (pdinput['op'] == 'A' ) & (pdinput['me'] == 'X' ),  
    (df['Alow'] >= df['Blow']) & (df['Alow'] <= df['Bhigh']),
    (df['Blow'] >= df['Alow']) & (df['Blow'] <= df['Ahigh'])
    ]

#    8    37   37    91

values2 = [1,1]



df['containscheck'] = np.select(conditions2, values2)


pd.set_option('display.max_rows', None)

#view DataFrame
print(df.to_string(index=False))

print(f"The answer for part two is:{df['containscheck'].sum()}")
