from machine import UART, Pin

uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
while True:
    uart1.write(b'HAAAAAAAAA\n\r')
    print("sending data to picoB")
    sleep(.1)