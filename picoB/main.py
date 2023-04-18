from machine import UART, Pin, PWM, ADC
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


def extend():
	thumb.duty_ns(1500000)
 	pointer.duty_ns(2000000)
	pinky.duty_ns(2000000)
	return False


pointer = initSer(15)
pinky = initSer(14)
thumb = initSer(16)


def poiCollaps():
    for nsec in range(pointer.duty_ns(), 650000, -50000):
        poiSen = round(currentSensor(27), 2)
        if poiSen > 2:
            pointer.duty_ns((nsec - 10000))
            break
        else:
            pointer.duty_ns(nsec)
    return True


def pinkyCollaps():
    for nsec in range(pinky.duty_ns(), 550000, -20000):
        pinkySen = round(currentSensor(26), 2)
        if pinkySen > 2:
            pinky.duty_ns((nsec - 10000))
            break
        else:
            pinky.duty_ns(nsec)
    return True

def thumbCollaps():
    for nsec in range(thumb.duty_ns(), 800000, -100000):
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

handState = False
uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5), timeout=100)
while True:
    emg = str(uart1.read(1))
    if '1' in emg:
        print(emg)
        if handState == False:
            _thread.start_new_thread(pinkyCollaps, ())
            thumbCollaps()
            poiCollaps()
            handState = True
    elif '0' in emg:
        print(emg)
        extend()
        handState = False