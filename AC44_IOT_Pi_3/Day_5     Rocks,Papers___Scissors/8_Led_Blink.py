
import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)

IO.setup(24,IO.OUT)
IO.setup(25,IO.OUT)
IO.setup(8,IO.OUT)
IO.setup(7,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(21,IO.OUT)

while True:
    IO.output(24,IO.HIGH)
    IO.output(25,IO.HIGH)
    IO.output(8,IO.HIGH)
    IO.output(7,IO.HIGH)
    IO.output(12,IO.HIGH)
    IO.output(16,IO.HIGH)
    IO.output(20,IO.HIGH)
    IO.output(21,IO.HIGH)
    
    time.sleep(1)
    IO.output(24,IO.LOW)
    IO.output(25,IO.LOW)
    IO.output(8,IO.LOW)
    IO.output(7,IO.LOW)
    IO.output(12,IO.LOW)
    IO.output(16,IO.LOW)
    IO.output(20,IO.LOW)
    IO.output(21,IO.LOW)
    time.sleep(1)
