from machine import Pin, ADC, PWM
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
  min = 350000
  max = 2000000
  pot_value = pot.read_u16()
  raw_value = abs(pot_value-30000)
  servo = PWM(Pin(15))
  servo.freq(50)
  sleep(0.01)
  if raw_value >= 2000:
    value = 1
  else:
    value = 0
  stream.append(value)
  stream.pop(0)
  avg = sum(stream)/8
  if avg >= 0.25:
    print(1)
    servo.duty_ns(max)
  else:
    print(0)
    servo.duty_ns(min)