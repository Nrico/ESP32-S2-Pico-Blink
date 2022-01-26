"""
LED example for Pico. Blinks external LED on and off.

REQUIRED HARDWARE:
* LED on pin IO10.
"""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.IO10)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

# Write your code here :-)
