from machine import UART, Pin
from time import sleep



def thumbCollaps():
    for nsec in range(thumb.duty_ns(), 1000000, -1000):
        thumbSen = .2
        if thumbSen > .350:
            thumb.duty_ns((nsec - 100000))
            print(thumbSen)
            print(thumb.duty_ns())
            break
        else:
            thumb.duty_ns(nsec)
            print(thumb.duty_ns())
            print(thumbSen)
    return True




uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
rxData = bytes()
while True:
    if uart1.any() > 0:
        rxData = uart1.read(1)
        rxData = rxData.decode()
    if rxData == '1':
        thumbCollaps()
    else:
        thumb.duty_ns(1500000)