import RPi.GPIO as gpio
import time
import datetime
from espeak import espeak
import Adafruit_BMP.BMP085 as BMP085
import smtplib
import Adafruit_DHT
import urllib2

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

server = smtplib.SMTP('smtp.gmail.com',587) #_THE SMTP ADDRESS AND SMTP PORT NUMBER OF GMAIL.
server.starttls()
url = 'http://thingspeak.com/update?key=GFM3RV5ONCXID580'   #_DO NOT FORGET TO CHANGE THE API KEY.

#_______________________________________________________________________________________________________________________________________________________

def bmp():
    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
    sleep(1)
#_______________________________________________________________________________________________________________________________________________________

def ultra():
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
#_______________________________________________________________________________________________________________________________________________________

def speech():
    
    speech =  'The Distance is ' + str(distance) +' cm'
    print(speech)

    time.sleep(0.55) #To ensure there's a gap between the visual and the switch press.
    
    if (gpio.input(switch)== True):
        espeak.synth(speech)

    time.sleep(3) #To ensure a delay between the audio output and the next reading
#_______________________________________________________________________________________________________________________________________________________

def dht():
    sensor =  Adafruit_DHT.DHT11
    pin = 17
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print humidity
        print temperature
#_______________________________________________________________________________________________________________________________________________________

def mail():
    server = smtplib.SMTP('smtp.gmail.com',587) #_THE SMTP ADDRESS AND SMTP PORT NUMBER OF GMAIL.
    server.starttls()

    print 'Sending the Mail...'

    server.login('actest344@gmail.com','@ChoppyPi3')

    tuday = datetime.datetime.today()
    mytime = datetime.datetime.now()
    
    mymsg = 'Hello There!:)\nChoppy recorded the following data with the help of a Pi3 & some sensors on {}-{}-{} at {}:{}:{}.\nHe mails you the data using the SMTP Protocol.\nTemperature = {}\nHumidity = {}\n'.format(tuday.year,tuday.month,tuday.day,mytime.hour,mytime.minute,mytime.second,temperature,humidity)
    print mymsg

    server.sendmail('actest344','abolishastri@gmail.com',mymsg)
    server.sendmail('actest344','shitalk8184@gmail.com',mymsg)
    server.sendmail('actest344','tanvigupte.13@gmail.com',mymsg)
    server.sendmail('actest344','ritusarwade@gmail.com',mymsg)
        
    server.quit()

    print 'Mails sent!'

    time.sleep(15)
#_______________________________________________________________________________________________________________________________________________________

def ldr():
    gpio.setup(4,gpio.OUT)
    gpio.output(4,gpio.LOW)
    time.sleep(0.5)

    gpio.setup(4,gpio.IN)

    while(gpio.input(4) == False):
        count+=1
        
    count = 0
#_______________________________________________________________________________________________________________________________________________________
