import pandas as pd

reviews = pd.Series([1.6, 2.6, 4.9, 5.6])
print(reviews)
print(reviews[1])


print(reviews.count())
print(reviews.mean())
print(reviews.min())
print(reviews.max())
print(reviews.std())

reviews = pd.Series([1.6, 2.6, 4.9, 5.6], index=['Python', 'java', 'django', 'devops'])
print(reviews)

reviews = pd.Series({'Python':1.6,'java':2.6,'django':4.9,'devops':5.6})
print(reviews)

print(reviews['Python'])
print(reviews.Python)

print(reviews.values)
print(reviews.index)


reviews = pd.Series(['Python', 'java','django','devops'])
print(reviews)
print(reviews.str.upper())
print(reviews.str.contains('ava'))


reviews = pd.Series([1.6, 2.6, 4.9, 5.6])
print(reviews.describe())