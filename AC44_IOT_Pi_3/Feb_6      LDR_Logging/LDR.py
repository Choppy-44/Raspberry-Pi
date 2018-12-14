import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

count = 0
gpio.setup(4,gpio.OUT)
gpio.output(4,gpio.LOW)
time.sleep(0.5)

gpio.setup(4,gpio.IN)

while(gpio.input(4) == False):
    count+=1

print count
count = 0
