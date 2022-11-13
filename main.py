from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(26))

while True:
  pot_value = pot.read_u16()
  if pot_value < 40000:
    print(pot_value)
  sleep(0.001)