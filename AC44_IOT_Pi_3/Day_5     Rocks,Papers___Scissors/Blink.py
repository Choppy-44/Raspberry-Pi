
import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)
IO.setup(24,IO.OUT)
while True:
    IO.output(24,IO.HIGH)
    time.sleep(1)
    IO.output(24,IO.LOW)
    time.sleep(1)
