import pandas as pd

score = {'Kohli': [100,50,70], 'Rohit' : [100, 88, 0],
         'Surya': [77, 110, 0], 'Jadeja': [99, 120, 8]}

df = pd.DataFrame(score)
print(df)

df = pd.DataFrame(score, index=['M1', 'M2', 'M3'])
print(df)

df = pd.DataFrame(score)
df.index=['M11', 'M12', 'M13']
print(df)

print('Koh')
print(df['Kohli'])
print(df.Kohli)

print('M11')
print(df.loc['M11'])
print('M11---')
print(df.iloc[1])
print('M11---M12')
print(df.loc['M11':'M12'])
print('M11---M11')
print(df.iloc[0:1])

print('M11---M13')
print(df.loc[['M11', 'M13']])

print('M11---M13')
print(df.iloc[[0, 2]])

print('M11---M13')
print(df.loc['M11':'M12', ['Kohli', 'Surya']])

print('M11---M13')
print(df.iloc[[0,2], [0,1]])


print('Scores >90')
print(df[df>=90])


print('Scores >90')
print(df[(df>=80) & (df<100)])

print(df.at['M11', 'Kohli'])
df.at['M11', 'Kohli'] = 98
print(df.at['M11', 'Kohli'])


print(df.iat[2,0])
df.iat[2,0] = 77
print(df.iat[2,0])


print(df.mean())

print(df.describe())
pd.set_option('display.precision', 2)
print(df.describe())

print('Transporse')
print(df.T)
print(df.T.describe())

print('Sort')
# By Match
print(df.sort_index())
print(df.sort_index(ascending=False))

# By player name
print(df.sort_index(axis=1))

# By match score
print(df.sort_values(by='M12',axis=1))

# By match score
print(df.sort_values(by='Rohit',axis=0))




