import RPi.GPIO as gpio
import time 
gpio.setmode (gpio.BCM)
gpio.setwarnings(False)

sw1 = 26
sw2 = 19

gpio.setup(24,gpio.OUT)
gpio.setup(25,gpio.OUT)
gpio.setup(8,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(20,gpio.OUT)
gpio.setup(21,gpio.OUT)
gpio.setup(sw1,gpio.IN)
gpio.setup(sw2,gpio.IN)

def all8():
    gpio.output(24,gpio.HIGH)
    gpio.output(25,gpio.HIGH)
    gpio.output(8,gpio.HIGH)
    gpio.output(7,gpio.HIGH)
    gpio.output(12,gpio.HIGH)
    gpio.output(16,gpio.HIGH)
    gpio.output(20,gpio.HIGH)
    gpio.output(21,gpio.HIGH)
        
    time.sleep(0.1)
    
    gpio.output(24,gpio.LOW)
    gpio.output(25,gpio.LOW)
    gpio.output(8,gpio.LOW)
    gpio.output(7,gpio.LOW)
    gpio.output(12,gpio.LOW)
    gpio.output(16,gpio.LOW)
    gpio.output(20,gpio.LOW)
    gpio.output(21,gpio.LOW)

    time.sleep(0.1)

def fourled():
    gpio.output(24,gpio.HIGH)
    gpio.output(25,gpio.HIGH)
    gpio.output(8,gpio.HIGH)
    gpio.output(7,gpio.HIGH)
    gpio.output(12,gpio.LOW)
    gpio.output(16,gpio.LOW)
    gpio.output(20,gpio.LOW)
    gpio.output(21,gpio.LOW)

    time.sleep(0.1)

    gpio.output(24,gpio.LOW)
    gpio.output(25,gpio.LOW)
    gpio.output(8,gpio.LOW)
    gpio.output(7,gpio.LOW)
    gpio.output(12,gpio.HIGH)
    gpio.output(16,gpio.HIGH)
    gpio.output(20,gpio.HIGH)
    gpio.output(21,gpio.HIGH)

    time.sleep(0.1)

flag = 0   
    
while True:
    inputval = gpio.input(26)
    if inputval == True and flag == 0 :
        flag = 10
        time.sleep(1)

    inputval1 = gpio.input(19)
    if inputval1 == True and flag == 10 :
        flag = 20
        time.sleep(1)

    if flag == 10:
        all8()

    if flag == 20:
        fourled()
    
    
 
    

    
