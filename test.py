from machine import Pin, ADC, PWM
from utime import sleep

pot = ADC(Pin(26))
while True:
    pot_value = pot.read_u16()
    raw_value = pot_value
    print(raw_value)
    sleep(0.1)