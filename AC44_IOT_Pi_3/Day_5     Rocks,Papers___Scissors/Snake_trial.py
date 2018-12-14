import RPi.GPIO as IO
import time
IO.setwarnings(False)

IO.setmode(IO.BCM)

IO.setup(24,IO.OUT)
IO.setup(25,IO.OUT)
IO.setup(8,IO.OUT)
IO.setup(7,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(21,IO.OUT)
IO.setup(26,IO.IN)

IO.output(24,IO.HIGH)
IO.output(25,IO.HIGH)
IO.output(8,IO.HIGH)
IO.output(7,IO.HIGH)
IO.output(12,IO.HIGH)
IO.output(16,IO.HIGH)
IO.output(20,IO.HIGH)
IO.output(21,IO.HIGH)

while True:
    IO.output(24,IO.LOW)
    time.sleep(0.45)
    IO.output(24,IO.HIGH)
    time.sleep(0.45)
    
  
    IO.output(25,IO.LOW)
    time.sleep(0.45)
    IO.output(25,IO.HIGH)
    time.sleep(0.45)
    
    
    IO.output(8,IO.LOW)
    time.sleep(0.45)
    IO.output(8,IO.HIGH)
    time.sleep(0.45)
    
   
    IO.output(7,IO.LOW)
    time.sleep(0.45)
    IO.output(7,IO.HIGH)
    time.sleep(0.45)
    
    
    IO.output(12,IO.LOW)
    time.sleep(0.45)
    IO.output(12,IO.HIGH)
    time.sleep(0.45)
    
   
    IO.output(16,IO.LOW)
    time.sleep(0.45)
    IO.output(16,IO.HIGH)
    time.sleep(0.45)
    
    
    IO.output(20,IO.LOW)
    time.sleep(0.45)
    IO.output(20,IO.HIGH)
    time.sleep(0.45)

    
    IO.output(21,IO.LOW)
    time.sleep(0.45)
    IO.output(21,IO.HIGH)
    time.sleep(0.45)
