import pigpio
from time import sleep

PB1_GPIO = 4
PB2_GPIO = 17
pi = pigpio.pi()
pi.set_pull_up_down(PB2_GPIO, pigpio.PUD_UP)

while True:
    if pi.read(PB1_GPIO) == 0:
        print('pb1 pressed')

    if pi.read(PB2_GPIO) == 0:
        print('pb2 pressed')
    sleep(.5)
