from machine import Pin, PWM
from time import sleep
import sys

#servo test script for Middle and Pointer fingers
#Made for troubleshooting ONLY

def initSer(pin):
  servo = PWM(Pin(pin))
  servo.freq(50)
  return servo

def extend():
	pointer.duty_ns(2000000)
	middle.duty_ns(2000000)
	return True

def collaps():
	pointer.duty_ns(400000)
	middle.duty_ns(550000)
	return False


middle = initSer(14)
pointer = initSer(17)

sleep(2)
collaps()
print("closed")
sleep(5)
extend()
print("opened")
sleep(5)
sys.exit()

