import board
import microcontroller
from time import sleep
from digitalio import DigitalInOut, Direction, Pull
from machine import Pin
from utime import sleep

pin = DigitalInOut(board.GP25)
pin.direction = Direction.OUTPUT

print("LED starts flashing...")
while True:
    pin.value = True
    sleep(300/1000) # sleep 1sec
    pin.value = False
    sleep(300/1000) # sleep 1sec


pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    pin.toggle()
    sleep(1) # sleep 1sec