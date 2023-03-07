from machine import Pin, ADC, PWM, UART
from utime import sleep
import _thread




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

def initSer(pin):
  servo = PWM(Pin(pin))
  servo.freq(50)
  return servo

def collaps():
  pointer.duty_ns(2000000)
  ring.duty_ns(1900000)
  return False

def extend():
 	pointer.duty_ns(400000)
	ring.duty_ns(350000)
	return True

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
	currentAvg = sum(currentList) / len(currentList)
	return currentAvg


def poiCollaps():
    for nsec in range(pointer.duty_ns(), 2000000, 20000):
        poiSen = currentSensor(28)
        if poiSen > .8:
            pointer.duty_ns((nsec - 100000))

            break
        else:
            pointer.duty_ns(nsec)
            poiSen = currentSensor(28)

    return True

def ringCollaps():
    for nsec in range(ring.duty_ns(), 2000000, 20000):
        ringSen = currentSensor(27)
        if ringSen > .8:
            ring.duty_ns((nsec - 500000))
            break
        else:
            ring.duty_ns(nsec)
    return True


def closeRing():
  emg = initEmg(26)
  stream = updateStream(stream, emg)
  avg = sum(stream)/len(stream)
  if avg >= .5:
      uart1.write(b'1\n\r')
      if handState == False:
        print(1)
        ringCollaps()
        handState = True
      elif handState == True:
        print(1)
  elif avg < .5:
    uart1.write(b'0\n\r')
    if handState == True:
      print(0)
      ring.duty_ns(350000)
      handState = False

pointer = initSer(14)
ring = initSer(16)
emg = initEmg(26)

stream = []
stream = initStream(stream, emg)
uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
handState = False

while True:
  emg = initEmg(26)
  stream = updateStream(stream, emg)
  avg = sum(stream)/len(stream)
  if avg > .5:
    uart1.write(b'1')
    if handState == False:
      print(1)
      _thread.start_new_thread(ringCollaps, ())
      poiCollaps()
      handState = True
  elif avg <= .5:
    uart1.write(b'0')
    if handState == True:
      print(0)
      pointer.duty_ns(400000)
      ring.duty_ns(350000)
      handState = False