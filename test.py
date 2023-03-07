from machine import Pin, ADC, PWM
from utime import sleep

def initEmg(pin):
    voltageList = []
    for i in range(0, 150):
        voltage = sensor = ADC(Pin(pin))
        data = sensor.read_u16()
        voltage = data * 3.3 / 65535
        voltageList.append(voltage)
    voltageAvg = sum(voltageList)/ len(voltageList)
    return voltageAvg

def initStream(xList, data):
  if data > 1.58 or data < 1.49:
    value = 1
  else:
    value = 0
  for i in range(0, 150):
    xList.append(value)
  return xList

def updateStream(xList, data):
  if data > 1.59 or data < 1.49:
    value = 1
  else:
    value = 0
  xList.append(value)
  xList.pop(0)
  return xList


emg = initEmg(26)
stream = []
stream = initStream(stream, emg)
while True:
    emg = initEmg(26)
    stream = updateStream(stream, emg)
    avg = sum(stream)/len(stream)
    if avg >= 0.5:
        print(1)
    else:
        print(0)
