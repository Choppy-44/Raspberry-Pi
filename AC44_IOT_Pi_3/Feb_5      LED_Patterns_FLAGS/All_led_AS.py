import RPi.GPIO as gpio
import time 
gpio.setmode (gpio.BCM)
gpio.setwarnings(False)


gpio.setup(24,gpio.OUT)
gpio.setup(25,gpio.OUT)
gpio.setup(8,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(20,gpio.OUT)
gpio.setup(21,gpio.OUT)

for i in range(10):
    gpio.output(24,gpio.HIGH)
    gpio.output(25,gpio.HIGH)
    gpio.output(8,gpio.HIGH)
    gpio.output(7,gpio.HIGH)
    gpio.output(12,gpio.HIGH)
    gpio.output(16,gpio.HIGH)
    gpio.output(20,gpio.HIGH)
    gpio.output(21,gpio.HIGH)

    time.sleep(1)

    gpio.output(24,gpio.LOW)
    gpio.output(25,gpio.LOW)
    gpio.output(8,gpio.LOW)
    gpio.output(7,gpio.LOW)
    gpio.output(12,gpio.LOW)
    gpio.output(16,gpio.LOW)
    gpio.output(20,gpio.LOW)
    gpio.output(21,gpio.LOW)

    time.sleep(1)

    
