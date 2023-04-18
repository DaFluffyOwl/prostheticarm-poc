from machine import Pin, ADC, PWM
from utime import sleep

class servo:
  def __init__(self, pin):
    self.pin = PWM(Pin(pin)).freq(50)
  
  def open():
    self.duty_ns(2000000)
    return 0
  
  def close():
    self.duty_ns(350000)

class emg:
  def __init__(self, pin):
    self.pin = ADC(Pin(26))
