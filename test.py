from machine import Pin, ADC, PWM
from utime import sleep
import math

def rms(xList):
  xList.sort()
  rms = xList[-1]/round((math.sqrt(2)/2), 4)
  return round(rms, 1)

def initStream(xList, data):
  for i in range(0, 100):
    xList.append(data)
  return xList

def updateStream(xList, data):
  xList.append(data)
  xList.pop(0)
  return xList


stream = []
stream = initStream(stream, 1)
while True:
  voltageList = []
  for i in range(0, 100):
    sensor = ADC(Pin(26))
    data = sensor.read_u16()
    voltage = (data / 65535) * 3.3
    voltageList.append(voltage)
  voltageRMS = rms(voltageList)
  stream = updateStream(stream, voltageRMS)
  avg = sum(stream)/len(stream)
  avg = round(avg, 2)
  print(avg)