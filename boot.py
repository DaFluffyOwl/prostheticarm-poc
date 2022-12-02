"""# boot.py -- run on boot-up
from machine import Pin, ADC
from utime import sleep

pot = ADC(Pin(26))
stream = []
pot_value = pot.read_u16()
raw_value = abs(pot_value-30000)
if raw_value >= 1000:
  value = 1
else:
  value = 0
sleep(0.08)
for i in range(0, 8):
  stream.append(value)

while True:
  pot_value = pot.read_u16()
  raw_value = abs(pot_value-30000)
  sleep(0.08)
  if raw_value >= 1000:
    value = 1
  else:
    value = 0
  stream.append(value)
  stream.pop(0)
  avg = sum(stream)/8
  if avg >= 0.25:
    print(1)
  else:
    print(0)"""

from machine import Pin, PWM
from time import sleep
from math import floor

pwm = PWM(Pin(0))
pwm.freq(50)
duty = 0
pwm.duty_u16(duty)
sleep(0.1)

min_duty = 2500
max_duty = 8050
min_degrees = 0
max_degrees = 180

def degrees_to_duty(degrees):
    # increment value per degree
    duty_step = ((max_duty - min_duty) / max_degrees)

    if degrees > max_degrees:
        degrees = max_degrees
    elif degrees < min_degrees:
        degrees = min_degrees

    # Get the duty value for the degrees
    duty = floor((duty_step * degrees) + min_duty)

    # Check value not out of bounds
    if duty > max_duty:
        duty = max_duty
    elif duty < min_duty:
        duty = min_duty

    return duty


while True:
    for degrees in range(min_degrees, max_degrees):
        print(degrees)
        duty = degrees_to_duty(degrees)
        pwm.duty_u16(duty)
        sleep(0.1)
    for degrees in range(max_degrees, min_degrees, -1):
        print(degrees)
        duty = degrees_to_duty(degrees)
        pwm.duty_u16(duty)
        sleep(0.1)