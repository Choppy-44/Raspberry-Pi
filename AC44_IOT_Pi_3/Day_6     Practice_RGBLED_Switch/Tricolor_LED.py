
import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)

IO.setup(20,IO.OUT)
IO.setup(25,IO.OUT)
IO.setup(24,IO.OUT)
IO.setup(6,IO.LOW)

while True:
    IO.output(24,IO.LOW)
    IO.output(20,IO.LOW)
    IO.output(25,IO.LOW)
    time.sleep(1)

    IO.output(24,IO.LOW)
    IO.output(20,IO.LOW)
    IO.output(25,IO.HIGH)
    time.sleep(1)

    IO.output(25,IO.LOW)
    IO.output(20,IO.HIGH)
    IO.output(24,IO.LOW)
    time.sleep(1)
    
    IO.output(20,IO.LOW)
    IO.output(24,IO.HIGH)
    IO.output(25,IO.LOW)
    time.sleep(1)

    IO.output(24,IO.LOW)
    IO.output(20,IO.HIGH)
    IO.output(25,IO.HIGH)
    time.sleep(1)

    IO.output(20,IO.LOW)
    IO.output(24,IO.HIGH)
    IO.output(25,IO.HIGH)
    time.sleep(1)

    IO.output(25,IO.LOW)
    IO.output(20,IO.HIGH)
    IO.output(24,IO.HIGH)
    time.sleep(1)

    IO.output(24,IO.HIGH)
    IO.output(20,IO.HIGH)
    IO.output(25,IO.HIGH)
    time.sleep(1)


    
