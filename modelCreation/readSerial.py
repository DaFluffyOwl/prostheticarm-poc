import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14101', baudrate=115200, timeout=1)
queue = []

for i in range(0, 8):
    data = str(ser.readline())
    data = data.replace('b', '')
    data = data.replace('\'', '')
    data = data.replace('\\', '')
    data = data.replace('rn', '')
    queue.append(data)
    time.sleep(0.01)
while True:
    for i in range(0, 8):
        data = str(ser.readline())
        data = data.replace('b', '')
        data = data.replace('\'', '')
        data = data.replace('\\', '')
        data = data.replace('rn', '')
        queue.append(data)
        time.sleep(0.01)
        print(queue)
        queue.pop(0)
        