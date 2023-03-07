from machine import UART, Pin
from time import sleep

uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
while True:
    rxData = bytes()
    while uart1.any() > 0:
        rxData += uart1.read(1)
    print(rxData.decode("utf-8"))
    sleep(.1)