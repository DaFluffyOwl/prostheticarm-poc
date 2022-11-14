from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataSet = pd.read_csv('modelCreation/newFullset.csv')
conv_arr= dataSet.values
X = dataSet.drop(columns='handstate').values
y = np.delete(conv_arr,[0,2],axis=1).ravel()
x_trained, x_test, y_trained, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=13)
model.fit(x_trained, y_trained)

predictions = model.predict(x_test)
predictionsDf = pd.DataFrame(predictions.tolist())
predictionsDf.to_csv('predictions.csv')
print(predictionsDf.head(10))
acc = accuracy_score(y_test, predictions)
print(acc)

values = np.delete(conv_arr,[1,2],axis=1) 
values_duplicated = np.delete(conv_arr,[0,1],axis=1) 
values = values.ravel()
values_duplicated = values_duplicated.ravel()

plt.scatter(x = dataSet["values"].values.flatten(), y = dataSet["values_duplicated"].values.flatten())
plt.show()