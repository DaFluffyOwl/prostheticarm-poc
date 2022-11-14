from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import serial
import time


ser = serial.Serial('/dev/cu.usbmodem14101', baudrate=115200, timeout=1)
dataSet = pd.read_csv('modelCreation/newFullset.csv')
conv_arr= dataSet.values
X = dataSet.drop(columns='handstate').values
y = np.delete(conv_arr,[0,2],axis=1).ravel()
x_trained, x_test, y_trained, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_trained, y_trained)

stream = []

for i in range (0, 8):
    data = str(ser.readline())
    data = data.replace('b', '')
    data = data.replace('\'', '')
    data = data.replace('\\', '')
    data = data.replace('rn', '')
    data = pd.DataFrame({"data0":[data],"data1":[data]})
    predictions = model.predict(data.values)
    stream.append(predictions)

while True:
    data = str(ser.readline())
    data = data.replace('b', '')
    data = data.replace('\'', '')
    data = data.replace('\\', '')
    data = data.replace('rn', '')
    data = pd.DataFrame({"data0":[data],"data1":[data]})
    predictions = model.predict(data.values)
    stream.append(predictions)
    stream.pop(0)
    avg = sum(stream)/len(stream)
    if avg >= .25:
        print(1)
    else:
        print(0)
