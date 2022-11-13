import pandas as pd

length = []
for i in range(0, 4000):
    length.append(0)

length_closed = []
for i in range(0, 4000):
    length_closed.append(1)

openDf = pd.read_csv('openHandDataset.csv')
closedDf = pd.read_csv('closedHandDataset.csv')
openTestSet = pd.read_csv('opentestSet.csv')

frames = [openDf, closedDf]
fullset = pd.concat(frames)
fullset = fullset.rename(columns={'set': 'values'})
fullset["values_squared"] = fullset.loc[:,'values']
fullset.to_csv('fullDataset.csv', index=False)
openTestSet['set_squared'] = openTestSet.loc[:,'set']
openTestSet.to_csv('openTestSet.csv', index=False)

print(openDf.head(10))
print(closedDf.head(10))
print(openTestSet.head(10))