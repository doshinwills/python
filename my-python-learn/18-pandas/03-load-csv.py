import pandas as pd

csv = pd.read_csv('test.csv',)
print(csv)

csv = pd.read_csv('test1.csv', names = ['LatD', 'LatM', 'LatS', 'NS'])
print(csv)


csv.to_csv('result.csv')
csv.to_csv('result1.csv', index=False)
