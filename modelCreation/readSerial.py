import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14101', baudrate=115200, timeout=1)

while True:
    data = str(ser.readline())
    data = data.replace('b', '')
    data = data.replace('\'', '')
    data = data.replace('\\', '')
    data = data.replace('rn', '')
    print(data)
    time.sleep(0.01)