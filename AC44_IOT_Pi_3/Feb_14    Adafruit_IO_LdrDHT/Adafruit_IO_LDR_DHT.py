from Adafruit_IO import *
import time
import Adafruit_DHT
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
ldr = 0

sensor =  Adafruit_DHT.DHT11  #_DHT11 GPIO SETUP
pin = 17

l1 = 24
l2 = 8

gpio.setup(l1,gpio.OUT)
gpio.setup(l2,gpio.OUT)

aio = Client('fc2b2990e634490385dccf451583c78b')

gpio.output(l1,gpio.HIGH)
gpio.output(l2,gpio.HIGH)

while True:
    ldr = 0
    hum,temp = Adafruit_DHT.read_retry(sensor,pin)                                    #_DHT INITIATED
    print 'Humidity = ',hum
    print 'Temperature = ',temp
    
    gpio.setup(4,gpio.OUT)
    gpio.output(4,gpio.LOW)
    time.sleep(0.5)
    
    gpio.setup(4,gpio.IN)

    while(gpio.input(4) == False):
        ldr+=1

    print 'LDR Count = ',ldr                                                          #_LDR INITIATED

    aio.send('temp',temp)
    time.sleep(0.5)
    aio.send('hum',hum)
    time.sleep(0.5)
    aio.send('ldr',ldr)
    time.sleep(0.5)

    led1 = aio.receive('sw1')
    print led1.value
    led2 = aio.receive('sw2')
    print led2.value
        
    if led1.value == 'ON':
        gpio.output(l1,gpio.LOW)
    elif led1.value == 'OFF':
        gpio.output(l1,gpio.HIGH)

    if led2.value == 'ON':
        gpio.output(l2,gpio.LOW)
    elif led2.value == 'OFF':
        gpio.output(l2,gpio.HIGH)
        

    

  
