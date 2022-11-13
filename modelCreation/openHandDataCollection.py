import serial
import time
import pandas as pd

ser = serial.Serial('/dev/cu.usbmodem14101', baudrate=115200, timeout=1)
opendf = pd.DataFrame()
closedDf = pd.DataFrame()
temp_list_open = []
temp_list_closed = []
for i in range(0, 4):
    for j in range(0, 1000):
            data = str(ser.readline())
            data = data.replace('b', '')
            data = data.replace('\'', '')
            data = data.replace('\\', '')
            data = data.replace('rn', '')
            temp_list_open.append(data)
            print(j)
    for x in range(0, 1000):
            data = str(ser.readline())
            data = data.replace('b', '')
            data = data.replace('\'', '')
            data = data.replace('\\', '')
            data = data.replace('rn', '')
            temp_list_closed.append(data)
            print(x)
        
opendf.insert(0, 'set' , temp_list_open)
closedDf.insert(0, 'set', temp_list_closed)


print(opendf)
opendf.to_csv('openhandDataset.csv')
closedDf.to_csv('closedHandDataCollection.csv')