import RPi.GPIO as gpio
import urllib2
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

url = 'http://thingspeak.com/update?key=DGF2MDAXEC0CF5B4'

ldr = 0

while True:
    gpio.setup(4,gpio.OUT)
    gpio.output(4,gpio.LOW)
    time.sleep(0.5)
    
    gpio.setup(4,gpio.IN)

    while(gpio.input(4) == False):
        ldr+=1

    mulldr = ldr*10
    divldr = ldr/10

    print ldr
    print mulldr
    print divldr

    myurl = url + '&field1=' + str(ldr) + '&field2=' + str(mulldr) + '&field3=' + str(divldr)
    response = urllib2.urlopen(myurl)
    print response.code
    time.sleep(15)

    ldr = 0
    
   
    
