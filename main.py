from machine import Pin, ADC, PWM
from utime import sleep




def initEmg(pin):
  sensor = ADC(Pin(26))
  return abs(sensor.read_u16() - 30000)

def initStream(xList, data):
  if data >= 1000:
    value = 1
  else:
    value = 0
  for i in range(0, 8):
    xList.append(value)
  return xList

def updateStream(xList, data):
  if data >= 2000:
    value = 1
  else:
    value = 0
  xList.append(value)
  xList.pop(0)
  return xList

def initSer(pin):
  servo = PWM(Pin(pin))
  servo.freq(50)
  return servo

def extend(ser):
  ser.duty_ns(350000)
  return False

def collaps(ser):
  ser.duty_ns(2000000)
  return True


emg = initEmg(26)
stream = []
stream = initStream(stream, emg)


while True:
  min = 350000
  max = 2000000
  emg = initEmg(26)
  pointer = initSer(15)
  pinky = initSer(14)
  sleep(0.01)
  stream = updateStream(stream, emg)
  avg = sum(stream)/8
  if avg >= 0.25:
    print(1)
    collaps(pointer)
    extend(pinky)
  else:
    print(0)
    extend(pointer)
    collaps(pinky)