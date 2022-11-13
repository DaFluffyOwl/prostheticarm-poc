import serial
import time
import pandas as pd

ser = serial.Serial('/dev/cu.usbmodem14101', baudrate=115200, timeout=1)
opendf = pd.DataFrame()

for i in range(0, 5):
    temp_list = []
    print(i)
    for j in range(0, 100):
            data = str(ser.readline())
            data = data.replace('b', '')
            data = data.replace('\'', '')
            data = data.replace('\\', '')
            data = data.replace('rn', '')
            temp_list.append(data)
            print(j)
        
    opendf.insert(0, 'set' + str(i+1) , temp_list)

print(opendf)
opendf.to_csv('closedtestSet.csv', index=False)