import thread
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

switch = 26
gpio.setup(24,gpio.OUT)
gpio.setup(25,gpio.OUT)
gpio.setup(8,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(20,gpio.OUT)
gpio.setup(21,gpio.OUT)
gpio.setup(switch,gpio.IN,pull_up_down=gpio.PUD_DOWN)

def check(threadname,delay):
    if gpio.input(switch) == 1 :
        return True

def all8():
    gpio.output(24,gpio.HIGH)
    gpio.output(25,gpio.HIGH)
    gpio.output(8,gpio.HIGH)
    gpio.output(7,gpio.HIGH)
    gpio.output(12,gpio.HIGH)
    gpio.output(16,gpio.HIGH)
    gpio.output(20,gpio.HIGH)
    gpio.output(21,gpio.HIGH)
        
    if check("Thread1",1) == True:
        fourled()
        
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

        
def fourled():
    gpio.output(24,gpio.HIGH)
    gpio.output(25,gpio.HIGH)
    gpio.output(8,gpio.HIGH)
    gpio.output(7,gpio.HIGH)
    gpio.output(12,gpio.LOW)
    gpio.output(16,gpio.LOW)
    gpio.output(20,gpio.LOW)
    gpio.output(21,gpio.LOW)

    if check("Thread1",1) == True:
        all8()
        
    time.sleep(1)

    gpio.output(24,gpio.LOW)
    gpio.output(25,gpio.LOW)
    gpio.output(8,gpio.LOW)
    gpio.output(7,gpio.LOW)
    gpio.output(12,gpio.HIGH)
    gpio.output(16,gpio.HIGH)
    gpio.output(20,gpio.HIGH)
    gpio.output(21,gpio.HIGH)

    time.sleep(1)

   
thread.start_new_thread(check,("Thread1",1))

while True:
    all8()
