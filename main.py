from machine import Pin, ADC, PWM
from utime import sleep


min = 1000000
max = 2000000

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
pwm = PWM(Pin(15))
pwm.freq(50)
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
    pwm.duty_ns(max)
  else:
    print(0)
    pwm.duty_ns(min)