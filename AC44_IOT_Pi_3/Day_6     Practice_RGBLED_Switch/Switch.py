import RPi.GPIO as IO
import time
IO.setmode(IO.BCM)
IO.setup(26,IO.IN,pull_up_down = IO.PUD_DOWN)
IO.setup(18,IO.OUT)
count = 0
while True:
    inputVal = IO.input(26)
    if inputVal == True:
        count += 1
        print ('Count' + str(count) + 'Times')
        IO.output(18,IO.HIGH)
        time.sleep(0.1)
        IO.output(18,IO.LOW)
        time.sleep(0.1)
