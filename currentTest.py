#script to test the current function


from machine import Pin, PWM
from time import sleep
import sys

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

while True:
	poiSen = currentSensor(27) #defining a sensor will always return the avg current
	print(poiSen)