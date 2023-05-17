from machine import Pin, ADC, PWM
from time import sleep
import _thread

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
	currentAvg = abs(sum(currentList) / len(currentList))
	return currentAvg


def initSer(pin):
  servo = PWM(Pin(pin))
  servo.freq(50)
  return servo


def collaps():
    pointer.duty_ns(1500000)
    middle.duty_ns(350000)
    ring.duty_ns(1900000)
    pinky.duty_ns(550000)
    sleep(1)
    thumb.duty_ns(1000000)
    return True


def extend():
    thumb.duty_ns(1700000)
    sleep(1)
    pointer.duty_ns(2000000)
    middle.duty_ns(2000000)
    ring.duty_ns(350000)
    pinky.duty_ns(2000000)
    return False


pointer = initSer(15)
middle = initSer(14)
ring = initSer(17)
pinky = initSer(14)
thumb = initSer(16)


def poiCollaps():
    for nsec in range(pointer.duty_ns(), 650000, -20000):
        poiSen = round(currentSensor(27), 2)
        if poiSen > 2:
            pointer.duty_ns((nsec - 100000))
            print(poiSen)
            print(pointer.duty_ns())
            print("object grabbed")
            break
        else:
            pointer.duty_ns(nsec)
            print(pointer.duty_ns())
            print(poiSen)
    return True

def ringCollaps():
    for nsec in range(ring.duty_ns(), 2000000, 50000):
        ringSen = round(currentSensor(27), 2)
        if ringSen > 2:
            ring.duty_ns((nsec - 100000))
            print(ringSen)
            print(ring.duty_ns())
            print("object grabbed")
            break
        else:
            ring.duty_ns(nsec)
            print(ring.duty_ns())
            print(ringSen)
    return True

def thumbCollaps():
    for nsec in range(thumb.duty_ns(), 500000, -20000):
        thumbSen = round(currentSensor(28), 2)
        if thumbSen > .750:
            thumb.duty_ns((nsec - 10000))
            print(thumbSen)
            print(thumb.duty_ns())
            print("object grabbed")
            break
        else:
            thumb.duty_ns(nsec)
            print(thumb.duty_ns())
            print(thumbSen)
    return True


def pinkyCollaps():
    for nsec in range(thumb.duty_ns(), 550000, -50000):
        pinkySen = round(currentSensor(26), 2)
        if pinkySen > 2:
            pinky.duty_ns((nsec - 10000))
            print(pinkySen)
            print(pinky.duty_ns())
            print("object grabbed")
            break
        else:
            pinky.duty_ns(nsec)
            print(pinky.duty_ns())
            print(pinkySen)
    return True

def midCollaps():
    for nsec in range(middle.duty_ns(), 800000, -20000):
        midSen = round(currentSensor(28), 2)
        if midSen > 2:
            middle.duty_ns((nsec - 10000))
            print(midSen)
            print(middle.duty_ns())
            print("object grabbed")
            break
        else:
            middle.duty_ns(nsec)
            print(middle.duty_ns())
            print(midSen)
    return True


#_thread.start_new_thread(ringCollaps, ())
#ringCollaps()
ringCollaps()
sleep(5)
print("closing")
extend()
sleep(2)
sys.exit()
