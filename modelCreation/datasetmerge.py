import pandas as pd


openDf = pd.read_csv('modelCreation/openHandDataset.csv')
closedDf = pd.read_csv('modelCreation/closedHandDataset.csv')
openTestSet = pd.read_csv('modelCreation/opentestSet.csv')

frames = [openDf, closedDf]
fullset = pd.concat(frames)
fullset = fullset.rename(columns={'set': 'values'})
fullset["values_duplicated"] = fullset.loc[:,'values']
fullset.to_csv('modelCreation/fullDataset.csv', index=False)
openTestSet['set_squared'] = openTestSet.loc[:,'set']
openTestSet.to_csv('modelCreation/openTestSet.csv', index=False)

print(openDf.head(10))
print(closedDf.head(10))
print(openTestSet.head(10))