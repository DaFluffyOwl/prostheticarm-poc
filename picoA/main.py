from machine import Pin, ADC, PWM, UART
from utime import sleep
import micropython
import _thread
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


def currentSensor(pin):
  AREF = 3.3 #internal voltage of RP2xxx
  DEFAULT_OUTPUT_VOLTAGE = 5/2 #for when current is 0 on a unipolar psu is Vcc/2
  MILLIVOLT_PER_AMPERE = 185 #mV/A output sensitivity for this particular sensro
  ERROR = 0.26 #for Error, tune as needed
  analogInputPin = ADC(pin) #Def ADC pin
  currentList = [] #create a list for finding an average of 150 samples
  for i in range(0, 150):
    analogValue = ADC.read_u16(analogInputPin)
    sensor_voltage = (analogValue / 65535) * AREF
    sensor_voltage = (sensor_voltage - DEFAULT_OUTPUT_VOLTAGE) * 1000
    dc_current = (sensor_voltage / MILLIVOLT_PER_AMPERE) - ERROR
    currentList.append(dc_current)
    sleep(0.003)
  currentAvg = round(abs(sum(currentList) / len(currentList)), 2)
  return currentAvg


def initSer(pin):
    servo = PWM(Pin(pin))
    servo.freq(50)
    return servo


def currentSensor(pin):
    AREF = 3.3  # internal voltage of RP2xxx
    DEFAULT_OUTPUT_VOLTAGE = 5 / 2  # for when current is 0 on a unipolar psu is Vcc/2
    MILLIVOLT_PER_AMPERE = 185  # mV/A output sensitivity for this particular sensro
    ERROR = 0.26  # for Error, tune as needed
    analogInputPin = ADC(pin)  # Def ADC pin
    currentList = []  # create a list for finding an average of 150 samples
    for i in range(0, 150):
        analogValue = ADC.read_u16(analogInputPin)
        sensor_voltage = ((analogValue / 65535) * AREF)
        sensor_voltage = (sensor_voltage - DEFAULT_OUTPUT_VOLTAGE) * 1000
        dc_current = (sensor_voltage / MILLIVOLT_PER_AMPERE) - ERROR
        currentList.append(dc_current)
    currentAvg = abs(sum(currentList) / len(currentList))
    return currentAvg


def extend():
    pointer.duty_ns(2000000)
    middle.duty_ns(2000000)
    return True


pointer = initSer(17)
middle = initSer(14)

def poiCollaps():
    for nsec in range(pointer.duty_ns(), 400000, -20000):
        poiSen = round(currentSensor(27), 3)
        if poiSen > .8:
            pointer.duty_ns((nsec - 1000))
            print(poiSen)
            print(pointer.duty_ns())
            print("object grabbed")
            break
        else:
            pointer.duty_ns(nsec)
            print(pointer.duty_ns())
            print(poiSen)
    return True

def midCollaps():
    for nsec in range(middle.duty_ns(), 400000, -20000):
        midSen = round(currentSensor(28), 3)
        if midSen > .8:
            middle.duty_ns((nsec-1000))
            print("object grabbed")
        else:
            middle.duty_ns(nsec)
            print(middle.duty_ns())
            print(midSen)
    return True


def getStream(xList, pin):
  voltageList = []
  for i in range(0, 100):
    sensor = ADC(Pin(pin))
    data = sensor.read_u16()
    voltage = round((data / 65535),3) * 3.3
    voltageList.append(voltage)
  voltageRMS = rms(voltageList)
  xList = updateStream(stream, voltageRMS)
  return xList


handState = False
stream = []
stream = initStream(stream, 1)
while True:
  uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5), timeout = 100)
  stream = getStream(stream, 26)
  avg = sum(stream)/len(stream)
  avg = round(avg, 2)
  print(avg)
  if avg > 2.4:
    if handState == False:
      uart1.write(b'1')
      _thread.start_new_thread(midCollaps, ())
      poiCollaps()
      handState = True
    else:
      uart1.write(b'1')
  else:
    extend()
    handState = False
    uart1.write(b'0')
