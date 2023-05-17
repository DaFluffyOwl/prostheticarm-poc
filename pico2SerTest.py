from machine import Pin, PWM
from time import sleep
import sys

def initSer(pin):
  servo = PWM(Pin(pin))
  servo.freq(50)
  return servo

def extend():
	pinky.duty_ns(350000)
	ring.duty_ns(350000)
	sleep(1)
	thumb.duty_ns(1000000)
	return True

def collaps():
	thumb.duty_ns(1500000)
	sleep(1)
	pinky.duty_ns(2000000)
	ring.duty_ns(1900000)
	return False


pinky = initSer(14)
ring = initSer(15)
thumb = initSer(18)

sleep(2)
collaps()
print("closed")
sleep(5)
extend()
print("opened")
sleep(5)
sys.exit()


#pointer works as intended
#middle finger is opposite
#ring finger works as intended change duty cycle to 1900000 for it to draw less current
#pinky finger is opposite change duty cycle in extended from 350000 to 550000 to draw less current