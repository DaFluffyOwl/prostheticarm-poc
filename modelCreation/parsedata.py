import pandas as pd

fullDataset = pd.read_csv('modelCreation/fullDataset.csv')

fullDataset['values'] = fullDataset['values'].shift(1)
fullDataset['values'] = fullDataset['values'].fillna(0)
fullDataset['values'] = fullDataset['values'].astype('int')
fullDataset.to_csv('newFullset.csv', index=False)
print(fullDataset.head(10))