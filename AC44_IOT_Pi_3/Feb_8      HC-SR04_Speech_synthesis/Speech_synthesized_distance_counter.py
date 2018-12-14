from espeak import espeak
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

trig = 14
echo = 15
switch = 26

gpio.setup(switch,gpio.IN,pull_up_down = gpio.PUD_DOWN)
 
while True:
    gpio.setup(trig,gpio.OUT)
    gpio.setup(echo,gpio.IN)

    gpio.output(trig,gpio.LOW)
    time.sleep(1)

    gpio.output(trig,gpio.HIGH)
    time.sleep(0.0001)

    gpio.output(trig,gpio.LOW)
    
    while(gpio.input(echo) == False):
        start = time.time()
    while (gpio.input(echo) == True):
        end = time.time()

    duration = end - start
    dist = duration * 17150
    dist = round(dist,2)

    if (dist<200 and dist>0):
        distance = dist

    speech =  'The Distance is ' + str(distance) +' cm'
    print(speech)

    time.sleep(0.55) #To ensure there's a gap between the visual and the switch press.
    
    if (gpio.input(switch)== True):
        espeak.synth(speech)

    time.sleep(3) #To ensure a delay between the audio output and the next reading
    

    
