from machine import Pin, PWM, ADC
from time import sleep
import sys
import _thread


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


print("closing")
_thread.start_new_thread(midCollaps, ())
poiCollaps()
sleep(5)
print("opening")
extend()
sleep(2)
sys.exit()
