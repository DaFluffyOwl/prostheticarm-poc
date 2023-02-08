from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(15))

servo.freq(50)
while True:
	servo.duty_ns(2000000)
	print("open")
	sleep(5)
	servo.duty_ns(400000)
	print("closed")
	sleep(5)